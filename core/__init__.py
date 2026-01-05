"""
core package
------------
Contains all core domain logic for the system.

This package is framework-agnostic and follows SOLID principles.
"""

from .models import ResearchPaper, PaperSection, PaperChunk
from .pdf_parser import ResearchPDFParser
from .chunking import SectionChunker
from .embeddings import EmbeddingManager
from .vector_store import PaperVectorStore
from .retrieval import SemanticRetriever
from .llm_factory import get_llm
from .summarizer import PaperSummarizer
from .qa_engine import ResearchQAEngine
from .citation_graph import CitationGraph
from .trend_analyzer import TrendAnalyzer

__all__ = [
    "ResearchPaper",
    "PaperSection",
    "PaperChunk",
    "ResearchPDFParser",
    "SectionChunker",
    "EmbeddingManager",
    "PaperVectorStore",
    "SemanticRetriever",
    "get_llm",
    "PaperSummarizer",
    "ResearchQAEngine",
    "CitationGraph",
    "TrendAnalyzer",
]
