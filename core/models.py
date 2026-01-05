from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class PaperSection:
    section_name: str
    text: str

@dataclass
class ResearchPaper:
    paper_id: str
    title: str
    authors: List[str]
    abstract: str
    full_text: str
    year: Optional[int]
    venue: Optional[str]
    keywords: List[str]
    sections: List[PaperSection]
    references: List[str]

@dataclass
class PaperChunk:
    paper_id: str
    section: str
    content: str
    metadata: Dict
