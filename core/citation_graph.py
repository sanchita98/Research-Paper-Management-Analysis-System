"""
citation_graph.py
-----------------
Manages citation relationships between research papers.

Purpose:
- Track which paper cites which other papers
- Enable related-work discovery
- Support citation-based analytics

Design:
- Lightweight in-memory graph (can be replaced by Neo4j later)
- No dependency on vector search or LLMs
"""

from collections import defaultdict
from typing import List


class CitationGraph:
    """
    Represents a directed citation graph:
    Paper A ---> Paper B (A cites B)
    """

    def __init__(self):
        # adjacency list: paper_id -> list of cited paper titles
        self._citations = defaultdict(list)

    def add_citation(self, source_paper_id: str, cited_paper_title: str):
        """
        Add a citation edge from one paper to another.

        Args:
            source_paper_id (str): ID of the citing paper
            cited_paper_title (str): Title of the cited paper
        """
        self._citations[source_paper_id].append(cited_paper_title)

    def get_references(self, paper_id: str) -> List[str]:
        """
        Get all papers cited by a given paper.
        """
        return self._citations.get(paper_id, [])

    def get_all_citations(self):
        """
        Return the full citation graph.
        """
        return dict(self._citations)
