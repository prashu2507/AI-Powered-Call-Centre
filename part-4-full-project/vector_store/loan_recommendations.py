from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import json

class LoanRecommendationStore:
    """A class to store and retrieve student loan recommendations using vector similarity search.
    
    This class uses OpenAI embeddings and Chroma vector store to save loan recommendations
    and find similar past recommendations based on student details.
    """

    def __init__(self, persist_directory="./vector_db/recommendations"):
        """Initialize the loan recommendation store.

        Args:
            persist_directory (str): Directory path where the vector store will be persisted.
                Defaults to "./vector_db/recommendations".
        """
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings
        )

    def store_recommendation(self, student_details, recommendation, metadata=None):
        """Store a loan recommendation along with the student's details.

        Args:
            student_details (dict): Dictionary containing student information
            recommendation (str): The loan recommendation text
            metadata (dict, optional): Additional metadata to store. Defaults to None.
        """
        text = f"Student: {json.dumps(student_details)}\nRecommendation: {recommendation}"
        self.vectorstore.add_texts(
            texts=[text],
            metadatas=[metadata or {}]
        )

    def find_similar_recommendations(self, student_details, n_results=3):
        """Find similar past recommendations based on student details.

        Args:
            student_details (dict): Dictionary containing student information to match against
            n_results (int): Number of similar recommendations to return. Defaults to 3.

        Returns:
            list: List of similar recommendations found in the vector store
        """
        query = json.dumps(student_details)
        results = self.vectorstore.similarity_search(
            query=query,
            k=n_results
        )
        return results
