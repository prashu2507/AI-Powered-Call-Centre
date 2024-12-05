"""
This module provides a vector store for storing and retrieving meaningful conversations.
It uses embeddings and similarity search to find relevant past conversations that can
help provide better responses to students' loan-related questions.
"""

import json
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

class ConversationStore:
    """
    A class for storing and retrieving meaningful conversations using vector embeddings.
    
    This allows the loan counselor to reference past conversations when helping students,
    providing more relevant and personalized responses based on similar past interactions.
    """
    def __init__(self, persist_directory="./vector_db/conversations"):
        """
        Initialize the conversation store with embeddings and vector storage.

        Args:
            persist_directory (str): Directory path where conversations will be stored
        """
        self.embeddings = OpenAIEmbeddings(
            cache_folder="./embeddings_cache"
        )
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings,
            collection_name="loan_conversations"
        )

    def store_conversation(self, user_id: str, conversation: str, metadata: dict = None):
        """
        Store important conversation snippets with associated metadata.

        Args:
            user_id (str): Unique identifier for the student
            conversation (str): The conversation text to store
            metadata (dict): Additional information about the conversation
                           like student details, loan preferences etc.
        """
        # Initialize empty dict if metadata is None
        if metadata is None:
            metadata = {}

        # Handle string metadata by parsing JSON
        if isinstance(metadata, str):
            try:
                metadata = json.loads(metadata)
            except json.JSONDecodeError:
                metadata = {}

        # Ensure metadata is a dict for consistency
        if not isinstance(metadata, dict):
            metadata = {}

        # Add user_id to metadata for tracking conversations by student
        filtered_metadata = {
            **metadata,
            'user_id': user_id
        }

        # Filter metadata to only include simple types that can be stored
        filtered_metadata = {
            k: str(v) for k, v in filtered_metadata.items()
            if isinstance(v, (str, int, float, bool))
        }

        self.vectorstore.add_texts(
            texts=[conversation],
            metadatas=[filtered_metadata]
        )

    def find_similar_conversations(self, query: str, n_results: int = 3):
        """
        Find past conversations that are semantically similar to the query.

        Args:
            query (str): The text to find similar conversations for
            n_results (int): Number of similar conversations to return

        Returns:
            list: Similar conversations with their metadata, ordered by relevance
        """
        results = self.vectorstore.similarity_search(query, k=n_results)
        # Convert Document objects to dict with text and metadata for easier handling
        return [{"text": doc.page_content, "metadata": doc.metadata} for doc in results]
