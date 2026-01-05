from langchain_community.vectorstores import FAISS

class PaperVectorStore:
    def __init__(self, embedding_model):
        self.store = None
        self.embedding_model = embedding_model

    def index(self, chunks):
        self.store = FAISS.from_texts(
            [c.content for c in chunks],
            self.embedding_model,
            metadatas=[c.metadata for c in chunks]
        )

    def search(self, query, k=5):
        return self.store.similarity_search(query, k)
