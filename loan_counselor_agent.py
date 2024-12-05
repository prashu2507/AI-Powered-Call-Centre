"""
This module defines the LoanCounselorAgent class, which is responsible for providing
loan counseling services to students.

The LoanCounselorAgent uses AI models and conversation memory to:
- Generate personalized loan recommendations based on student details
- Maintain contextual conversations with students
- Search and match relevant lenders
- Store and retrieve past recommendations
- Provide follow-up question suggestions
"""
import os
import json
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any, Optional
from functools import lru_cache
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langsmith import traceable
from helpers import format_lenders_data
from prompts import QUERY_RECOMMENDATION_PROMPT, INITIAL_PROMPT
from utils.constant import LENDER_DATA
from vector_store.loan_recommendations import LoanRecommendationStore
from vector_store.lender_store import LenderStore
from vector_store.conversation_store import ConversationStore

load_dotenv()

class LoanCounselorAgent:
    """
    An AI-powered loan counselor that helps students understand their loan options.

    This class provides personalized loan counseling by:
    - Analyzing student details and requirements
    - Matching students with suitable lenders
    - Maintaining conversation context
    - Generating relevant recommendations and follow-up questions
    - Storing conversation history and recommendations for future reference

    Attributes:
        lenders (List[Dict]): Available loan providers and their details
        llm (ChatOpenAI): The AI language model for generating responses
        memory (Dict): Stores conversation history for each user
        recommendation_store (LoanRecommendationStore): Database of past recommendations
        lender_store (LenderStore): Searchable database of lenders
        conversation_store (ConversationStore): Stores full conversation histories
        executor (ThreadPoolExecutor): Handles parallel processing tasks
    """
    def __init__(self,
                 model: Optional[str] = None,
                 api_key: Optional[str] = None,
                 temperature: float = 0.6):
        """
        Initialize the loan counselor with necessary components.

        Args:
            model: The AI model name to use (defaults to environment variable)
            api_key: API key for the AI service (defaults to environment variable)
            temperature: Controls randomness in AI responses (0.0 to 1.0)
        """
        self.lenders = self.load_lenders()
        self.llm = self._initialize_llm(
            model or os.getenv("OPENAI_MODEL"),
            api_key or os.getenv("OPENAI_API_KEY"), 
            temperature
        )
        self.memory: Dict[str, ConversationBufferMemory] = {}
        self.prompt_template = self._initialize_prompt_template()
        self.recommendation_store = LoanRecommendationStore()
        self.lender_store = LenderStore()
        self.lender_store.index_lenders(self.lenders)
        self.conversation_store = ConversationStore()
        self.executor = ThreadPoolExecutor(max_workers=4)

    @staticmethod
    def _initialize_llm(model: str, api_key: str, temperature: float) -> ChatOpenAI:
        """
        Initialize the AI language model.

        Args:
            model: Name of the AI model to use
            api_key: API key for authentication
            temperature: Controls response randomness

        Returns:
            ChatOpenAI: Configured language model instance

        Raises:
            ValueError: If model or API key is missing
        """
        if not model or not api_key:
            raise ValueError("Model and API key must be provided")
        return ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=api_key
        )

    def get_user_memory(self, user_id: str) -> ConversationBufferMemory:
        """
        Get or create conversation memory for a specific user.

        Args:
            user_id: Unique identifier for the user

        Returns:
            ConversationBufferMemory: User's conversation memory
        """
        if user_id not in self.memory:
            self.memory[user_id] = ConversationBufferMemory(
                memory_key=f"conversation_history_{user_id}",
                return_messages=True
            )
        return self.memory[user_id]

    @staticmethod
    def _initialize_prompt_template() -> PromptTemplate:
        """
        Initialize the template for generating AI responses.

        Returns:
            PromptTemplate: Configured template for generating responses
        """
        return PromptTemplate(
            input_variables=["lenders_data", "student_details",
                           "conversation_history", "student_message"],
            template=INITIAL_PROMPT
        )

    @lru_cache(maxsize=1)
    def load_lenders(self) -> List[Dict[str, Any]]:
        """
        Load and cache lender information.

        Returns:
            List[Dict]: List of lender details
        """
        return LENDER_DATA

    def _get_conversation_history(self, user_id: str) -> List[Any]:
        """
        Retrieve conversation history for a user.

        Args:
            user_id: Unique identifier for the user

        Returns:
            List: Previous conversation messages
        """
        return self.get_user_memory(user_id).load_memory_variables({}).get(
            f'conversation_history_{user_id}', []
        )

    def _prepare_recommendation_inputs(
        self,
        student_details: Dict[str, Any],
        student_message: str,
        conversation_history: List[Any]
    ) -> Dict[str, Any]:
        """
        Prepare all necessary inputs for generating recommendations.

        Args:
            student_details: Student's information and requirements
            student_message: Current message from student
            conversation_history: Previous conversation context

        Returns:
            Dict: Prepared inputs for recommendation generation
        """
        # Get recommendations, lenders and format data in parallel
        futures = {
            'similar_recs': self.executor.submit(
                self.recommendation_store.find_similar_recommendations,
                student_details
            ),
            'matching_lenders': self.executor.submit(
                self.lender_store.search_lenders,
                f"{student_details['destination_country']} {student_details['loan_amount_needed']}"
            ),
            'formatted_lenders': self.executor.submit(format_lenders_data, self.lenders),
            'formatted_student': self.executor.submit(json.dumps, student_details, indent=2)
        }

        conversation_summary = [
            f"{msg.type}: {msg.content}" if hasattr(msg, 'content')
            else f"{msg.get('type', 'Unknown')}: {msg.get('content', '')}" if isinstance(msg, dict)
            else str(msg)
            for msg in conversation_history
        ]

        return {
            'lenders_data': futures['formatted_lenders'].result(),
            'student_details': futures['formatted_student'].result(),
            'similar_cases': str(futures['similar_recs'].result()),
            'matching_lenders': str(futures['matching_lenders'].result()),
            'student_message': student_message,
            'conversation_history': "\n".join(conversation_summary)
        }

    @traceable(project_name="loan-counselor-agent")
    def get_loan_recommendation(
        self,
        student_details: Dict[str, Any],
        student_message: str,
        user_id: str
    ) -> Dict[str, Any]:
        """
        Generate personalized loan recommendations and follow-up questions.

        Args:
            student_details: Student's information and requirements
            student_message: Current message from student
            user_id: Unique identifier for the student

        Returns:
            Dict: Contains AI response and recommended follow-up questions

        Raises:
            Returns error message if recommendation generation fails
        """
        try:
            user_memory = self.get_user_memory(user_id)
            conversation_history = self._get_conversation_history(user_id)

            inputs = self._prepare_recommendation_inputs(
                student_details,
                student_message,
                conversation_history
            )

            # Generate response and query recommendation in parallel
            response_future = self.executor.submit(
                self.llm.predict,
                self.prompt_template.format(**inputs)
            )
            query_rec_future = self.executor.submit(
                self.get_query_recommendation,
                student_message,
                user_id
            )

            response = response_future.result()
            
            # Save context and store recommendation in parallel
            self.executor.submit(
                user_memory.save_context,
                {"input": student_message},
                {"output": response}
            )
            self.executor.submit(
                self.recommendation_store.store_recommendation,
                student_details=student_details,
                recommendation=response,
                metadata={'user_id': user_id}
            )

            return {
                'response': response,
                'query_recommendation': query_rec_future.result()
            }

        except Exception as e:
            return {'error': f"An error occurred while generating a recommendation: {str(e)}"}

    @traceable(project_name="loan-counselor-agent")
    def get_query_recommendation(self, query: str, user_id: str) -> str:
        """
        Generate relevant follow-up questions based on conversation context.

        Args:
            query: Current question or message from student
            user_id: Unique identifier for the student

        Returns:
            str: Recommended follow-up questions or error message
        """
        try:
            conversation_history = self._get_conversation_history(user_id)
            prompt = QUERY_RECOMMENDATION_PROMPT.format(
                conversation_history=str(conversation_history),
                query=query
            )
            return self.llm.predict(prompt)

        except Exception as e:
            return f"An error occurred while generating question recommendations: {str(e)}"

    def reset_conversation(self, user_id: str) -> None:
        """
        Clear conversation history for a user.

        Args:
            user_id: Unique identifier for the student
        """
        self.memory.pop(user_id, None)
