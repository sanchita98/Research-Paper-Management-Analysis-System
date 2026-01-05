"""
summarizer.py
-------------
Generates structured academic summaries using Groq LLM.
Uses modern LangChain Runnable interface (NO LLMChain).
"""

from langchain_core.prompts import PromptTemplate
from core.llm_factory import get_llm


class PaperSummarizer:
    def __init__(self):
        self.llm = get_llm()

        self.prompt = PromptTemplate(
            template="""
You are an academic research assistant.

Summarize the paper using:
- Problem Statement
- Proposed Method
- Key Contributions
- Results
- Limitations

Text:
{text}
""",
            input_variables=["text"],
        )

        # Runnable chain (modern LangChain)
        self.chain = self.prompt | self.llm

    def summarize(self, text: str) -> str:
        """
        Generate a structured academic summary.
        """
        response = self.chain.invoke({"text": text})
        return response.content
