"""
app.py

This file runs the Streamlit user interface for the Research Paper Management and Analysis system.

The application helps users upload research papers and interact with them using AI.

What this app does:
Upload research papers in PDF format
Create a smart (semantic) index from the documents
Automatically generate easy-to-read summaries
Ask questions and get answers using a RAG-based AI model (Groq LLM)
Provides a simple and clean interface suitable for reviews and demos
"""

import os
import uuid
import streamlit as st

from core import (
    ResearchPDFParser,
    SectionChunker,
    EmbeddingManager,
    PaperVectorStore,
    SemanticRetriever,
    PaperSummarizer,
    ResearchQAEngine,
    TrendAnalyzer,
)
from services import (
    PaperIngestionService,
    SearchService,
    AnalysisService,
)
import streamlit as st
import os
import uuid

# ----------------------------
# 1. Page Configuration & Theme
# ----------------------------
st.set_page_config(
    page_title="Research Intel",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .stExpander { border: 1px solid #e6e9ef; border-radius: 0.5rem; background-color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# ----------------------------
# 2. Cached Resource Initialization
# ----------------------------
# These ensure heavy models don't reload on every button click
@st.cache_resource
def load_backend():
    # Replace these with your actual class imports
    return ResearchPDFParser(), SectionChunker(), EmbeddingManager(), TrendAnalyzer()

parser, chunker, embedder, trend_analyzer = load_backend()

# ----------------------------
# 3. Session State Management
# ----------------------------
state_keys = {
    "vector_store": None,
    "papers_loaded": False,
    "paper_text": "",
    "paper_summary": "",
    "chat_history": []
}

for key, default in state_keys.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ----------------------------
# 4. Sidebar - Paper Management
# ----------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2436/2436636.png", width=80)
    st.title("Research Library")
    st.info("Upload a PDF to begin your analysis.")
    
    uploaded_file = st.file_uploader(
        "Upload Research Paper", 
        type=["pdf"],
        help="Only PDF files are supported for semantic analysis."
    )
    
    if uploaded_file:
        if not st.session_state.papers_loaded:
            with st.status("🛠️ Indexing Paper...", expanded=True) as status:
                st.write("Extracting text sections...")
                os.makedirs("data/raw_papers", exist_ok=True)
                paper_id = str(uuid.uuid4())[:8]
                pdf_path = f"data/raw_papers/{paper_id}.pdf"

                with open(pdf_path, "wb") as f:
                    f.write(uploaded_file.read())

                sections = parser.extract_sections(pdf_path)
                st.session_state.paper_text = "\n\n".join(sec.text for sec in sections)

                st.write("Generating vector embeddings...")
                chunks = []
                for sec in sections:
                    chunks.extend(chunker.chunk(paper_id, sec.section_name, sec.text))

                vector_store = PaperVectorStore(embedder.model)
                vector_store.index(chunks)
                
                st.session_state.vector_store = vector_store
                st.session_state.papers_loaded = True
                status.update(label="✅ Indexing Complete!", state="complete", expanded=False)
        else:
            st.success("📍 Paper Loaded")

    st.divider()
    if st.button("🗑️ Clear Library"):
        st.session_state.clear()
        st.rerun()

# ----------------------------
# 5. Main UI Header
# ----------------------------
col1, col2 = st.columns([1, 6])
with col1:
    st.write("") # Spacer
with col2:
    st.title("🧠 Research Intelligence System")
    st.caption("LLM-Powered Semantic Search • Section-Aware Summarization • Evidence-Based Q&A")

# ----------------------------
# 6. Tabs Layout (The Workspace)
# ----------------------------
tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard", 
    "📝 Executive Summary", 
    "💬 Expert Chat"
])

# --- TAB 1: Dashboard ---
with tab1:
    if not st.session_state.papers_loaded:
        st.warning("Please upload a paper in the sidebar to view analysis.")
    else:
        st.subheader("Document Overview")
        c1, c2, c3 = st.columns(3)
        c1.metric("Character Count", len(st.session_state.paper_text))
        c2.metric("Reading Time", f"{len(st.session_state.paper_text)//3000} min")
        c3.metric("Status", "Indexed", delta="Ready")
        
        with st.expander("🔍 View Extracted Raw Text"):
            st.text_area("Preview", st.session_state.paper_text[:2000] + "...", height=300)

# --- TAB 2: Auto Summary ---
with tab2:
    if st.session_state.papers_loaded:
        st.subheader("Structured Abstract & Analysis")
        
        if st.button("✨ Generate AI Summary", type="primary"):
            with st.spinner("Analyzing document structure..."):
                summarizer = PaperSummarizer()
                st.session_state.paper_summary = summarizer.summarize(
                    st.session_state.paper_text[:8000]
                )

        if st.session_state.paper_summary:
            st.markdown("---")
            st.markdown(st.session_state.paper_summary)
            st.download_button("Download Summary", st.session_state.paper_summary, file_name="summary.md")
    else:
        st.info("Awaiting PDF upload...")

# --- TAB 3: Research Chat ---
with tab3:
    if st.session_state.papers_loaded:
        st.subheader("Interrogate the Evidence")
        
        # Chat-style Input
        query = st.chat_input("Ask a question about the methodology, results, or conclusion...")

        if query:
            with st.chat_message("user"):
                st.markdown(query)
            
            with st.chat_message("assistant"):
                with st.spinner("Scanning vector space..."):
                    retriever = SemanticRetriever(st.session_state.vector_store)
                    qa_engine = ResearchQAEngine(retriever)
                    answer = qa_engine.answer(query)
                    st.markdown(answer)
                    
                    # Optional: Show sources
                    with st.expander("View Source Context"):
                        st.caption("Retrieved relevant segments from the PDF for this answer.")
    else:
        st.info("Upload a paper to enable the RAG Chatbot.")

# ----------------------------
# 7. Footer
# ----------------------------
st.divider()
st.caption("Built with Groq LPU™ Inference • LangChain • Streamlit")