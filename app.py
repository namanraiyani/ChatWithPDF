# app.py
import streamlit as st
from functions import get_pdf_text, get_chunks, get_vector_store, user_input
from utils import create_sidebar

def main():
    st.title("PDF Q&A Chatbot with Google Generative AI")

    temperature = create_sidebar()

    uploaded_files = st.file_uploader("Upload your PDF(s)", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        st.write("Uploaded PDF(s):")
        for file in uploaded_files:
            st.write(file.name)

        with st.spinner("Processing..."):
            pdf_text = get_pdf_text(uploaded_files)
            text_chunks = get_chunks(pdf_text)
            get_vector_store(text_chunks)
            st.success("PDFs processed successfully and vector store created!")

    user_question = st.text_input("Ask a question about the PDFs:")

    if user_question:
        with st.spinner("Searching for the answer..."):
            answer = user_input(user_question, temperature)
            st.write("Reply: ", answer)

if __name__ == "__main__":
    main()