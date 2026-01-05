from langchain_text_splitters import RecursiveCharacterTextSplitter
from .models import PaperChunk

class SectionChunker:
    def __init__(self, chunk_size=800, overlap=150):
        self.chunk_size=chunk_size
        self.overlap=overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.overlap,
            length_function=len,
            separators=["\n\n","\n"," ",""]
        )

    def chunk(self, paper_id, section, text):
        return [
            PaperChunk(paper_id, section, c, {"section": section})
            for c in self.splitter.split_text(text)
        ]
