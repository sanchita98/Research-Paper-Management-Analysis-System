from langchain_community.document_loaders import PyPDFLoader
from .models import PaperSection

class ResearchPDFParser:
    def extract_sections(self, pdf_path):
        pages = PyPDFLoader(pdf_path).load()
        full_text = " ".join(p.page_content for p in pages)

        sections = []
        for name in ["Abstract", "Introduction", "Method", "Results", "Conclusion", "References"]:
            sections.append(PaperSection(name, full_text))

        return sections
