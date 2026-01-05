class PaperIngestionService:
    def __init__(self, parser, chunker, vector_store):
        self.parser = parser
        self.chunker = chunker
        self.vector_store = vector_store

    def ingest(self, pdf_path, paper_id):
        sections = self.parser.extract_sections(pdf_path)
        chunks = []

        for s in sections:
            chunks.extend(self.chunker.chunk(paper_id, s.section_name, s.text))

        self.vector_store.index(chunks)
