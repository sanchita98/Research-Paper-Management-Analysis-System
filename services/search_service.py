"""
search_service.py
-----------------
Handles semantic discovery of research papers.

Why this exists:
- UI should NOT talk directly to FAISS or retrievers
- Central place to add filters (year, keywords, venue)
- Keeps retrieval logic consistent across the app

SOLID:
- SRP: only search & discovery
- DIP: depends on retriever abstraction
"""

class SearchService:
    def __init__(self, retriever):
        """
        Args:
            retriever: SemanticRetriever instance
        """
        self.retriever = retriever

    def search(self, query: str, top_k: int = 5):
        """
        Perform semantic search across indexed papers.

        Args:
            query (str): Natural language query
            top_k (int): Number of results

        Returns:
            List of relevant document chunks
        """
        return self.retriever.retrieve(query, top_k)
