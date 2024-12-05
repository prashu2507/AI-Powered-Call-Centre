"""
This module provides a vector store for storing and retrieving lender information.
It uses embeddings and similarity search to find relevant lenders based on student
requirements and preferences.
"""

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

class LenderStore:
    """
    A class for storing and searching loan provider information using vector embeddings.
    
    This allows the loan counselor to find and recommend relevant lenders based on 
    students' specific needs, preferences and requirements.
    """
    def __init__(self, persist_directory="./vector_db/lenders"):
        """
        Initialize the lender store with embeddings and vector storage.

        Args:
            persist_directory (str): Directory path where lender data will be stored
        """
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings
        )

    def index_lenders(self, lenders):
        """
        Index lender information for semantic search capabilities.
        
        Creates text representations and metadata for each lender that can be 
        searched semantically to find matches for student requirements.

        Args:
            lenders (list): List of dictionaries containing lender information
                           including name, interest rates, maximum amounts etc.
        """
        texts = []
        metadatas = []

        for lender in lenders:
            text = f"{lender['name']} {lender['about']} Interest: {lender['interest_rate']}"
            # Convert complex data types to strings for storage
            metadata = {
                'name': str(lender['name']),
                'interest_rate': str(lender['interest_rate']),
                'maximum_amount': str(lender['maximum_amount']),
                'currency': str(lender['currency']),
                'country': str(lender['country']),
                'key_points': ', '.join(lender['key_points'])  # Convert list to string
            }
            texts.append(text)
            metadatas.append(metadata)
 
        self.vectorstore.add_texts(texts=texts, metadatas=metadatas)

    def search_lenders(self, query, n_results=5):
        """
        Search for lenders based on student requirements and preferences.

        Uses semantic similarity to find lenders that best match the student's needs.

        Args:
            query (str): Search query describing student's requirements
            n_results (int): Number of matching lenders to return (default: 5)

        Returns:
            list: Matching lender documents ordered by relevance
        """
        return self.vectorstore.similarity_search(query, k=n_results)
