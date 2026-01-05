"""
trend_analyzer.py
-----------------
Analyzes research trends across a collection of papers.

Purpose:
- Identify frequently occurring keywords
- Detect emerging topics over time
- Support research insight dashboards

Design:
- Pure analytics (no LLM, no vector DB)
- Easily testable and replaceable
"""

from collections import Counter
from typing import List


class TrendAnalyzer:
    """
    Performs keyword- and time-based trend analysis on papers.
    """

    def identify_trends(self, papers: List) -> List:
        """
        Identify top recurring keywords across papers.

        Args:
            papers (List[ResearchPaper]): Collection of papers

        Returns:
            List of (keyword, frequency)
        """
        all_keywords = []

        for paper in papers:
            if hasattr(paper, "keywords"):
                all_keywords.extend(paper.keywords)

        keyword_counts = Counter(all_keywords)
        return keyword_counts.most_common(10)

    def yearly_distribution(self, papers: List):
        """
        Analyze paper counts by publication year.

        Returns:
            Dict[year, count]
        """
        year_counts = Counter()

        for paper in papers:
            if paper.year:
                year_counts[paper.year] += 1

        return dict(year_counts)
