import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

from langchain.embeddings.ollama import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

from langchain_ollama import OllamaLLM

llm_model = "llama3.2:3b"
embed_model = "mxbai-embed-large:335m"


st.header("PDF to Text")

with st.sidebar:

    st.title("PDF to Text")
    st.markdown("This app extracts text from PDF files and displays it.")
    st.markdown(
        "None of the data is sent to any server. All processing is done locally."
    )
    st.markdown("Developed by [Alok Rajput](https://github.com/rajalok83)")
    st.markdown("---")
    st.markdown("## Upload your PDF file")
    pdf_file = st.file_uploader("Choose a PDF file", type="pdf")


if pdf_file is not None:
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    st.success("PDF file uploaded and text extracted successfully!")
    st.markdown("---")
    st.header("Extracted Text")
    st.text_area("Text", text, height=300)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks = text_splitter.split_text(text)
    st.success(f"Text split into {len(chunks)} chunks successfully!")
    st.markdown(f"## Text Split into {len(chunks)} Chunks")
    for i, chunk in enumerate(chunks):
        st.subheader(f"Chunk {i+1}")
        st.text_area(f"Chunk {i+1}", chunk, height=200)
    ollama_embeddings = OllamaEmbeddings(model=embed_model)

    try:
        test_embedding = ollama_embeddings.embed_documents([chunks[0]])
        if (
            not test_embedding or len(test_embedding) != 1
        ):  # Check if we got a proper embedding
            raise ValueError("Embedding generation failed.")
    except Exception as e:
        st.error(f"Error initializing embeddings: {e}")
    else:
        # Create a FAISS index using the embedding model directly
        knowledge_base = FAISS.from_texts(chunks, ollama_embeddings)
        st.success("FAISS knowledge base created successfully!")


user_question = st.text_input("Ask a question about the PDF:")
if user_question and pdf_file is not None:
    docs = knowledge_base.similarity_search(user_question)
    llm = OllamaLLM(model=llm_model)
    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=user_question)
    st.write("## Answer")
    st.write(response)
