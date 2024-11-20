# PDF Q&A Chatbot with Google Generative AI

This project uses Streamlit, LangChain, and Google Generative AI to build a chatbot that answers questions based on the content of uploaded PDFs. Once the user uploads a PDF file, the app processes the content, splits it into chunks, and stores the text in a vector store for efficient question-answering. The user can then ask questions related to the PDF, and the system will return detailed answers based on the content.

## Features

- **PDF Upload**: Upload one or multiple PDFs.
- **Automatic Processing**: As soon as a PDF is uploaded, it is processed automatically by extracting text, splitting it into chunks, and storing it in a vector store (FAISS).
- **Question Answering**: Ask a question, and the system will return the most relevant answer from the uploaded PDF(s).
- **Temperature Control**: A slider in the sidebar allows you to control the "temperature" (randomness) of the generative model.
- **Use of Google Generative AI**: Leverages the Google Generative AI API for embedding generation and question-answering.

## Requirements

To run this project locally, you will need the following Python packages:

- `streamlit`
- `langchain`
- `PyPDF2`
- `faiss-cpu`
- `langchain-google-genai`
- `google-generativeai`
- `python-dotenv`

To install the required dependencies, you can use the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
