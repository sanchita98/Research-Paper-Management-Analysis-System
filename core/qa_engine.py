from core.llm_factory import get_llm

class ResearchQAEngine:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = get_llm()

    def answer(self, question):
        docs = self.retriever.retrieve(question)
        context = "\n\n".join(d.page_content for d in docs)

        return self.llm.invoke(
            f"Context:\n{context}\n\nQuestion:{question}"
        ).content
