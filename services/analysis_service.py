"""
analysis_service.py
-------------------
Provides higher-level research intelligence features.

This service sits ABOVE retrieval and LLM logic and
combines multiple capabilities into user-facing actions.

Responsibilities:
- Paper summarization
- Context-aware research Q&A
- Trend & keyword analysis

SOLID:
- SRP: analysis only
- OCP: easy to add more analytics later
"""

class AnalysisService:
    def __init__(self, summarizer, qa_engine, trend_analyzer):
        """
        Args:
            summarizer: PaperSummarizer instance
            qa_engine: ResearchQAEngine instance
            trend_analyzer: TrendAnalyzer instance
        """
        self.summarizer = summarizer
        self.qa_engine = qa_engine
        self.trend_analyzer = trend_analyzer

    def summarize_paper(self, paper_text: str) -> str:
        """
        Generate a structured academic summary of a paper.
        """
        return self.summarizer.summarize(paper_text)

    def answer_question(self, question: str) -> str:
        """
        Answer a research question using RAG.
        """
        return self.qa_engine.answer(question)

    def analyze_trends(self, papers):
        """
        Identify emerging research trends across papers.
        """
        return self.trend_analyzer.identify_trends(papers)
