class SemanticRetriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query, top_k=5):
        return self.vector_store.search(query, top_k)
