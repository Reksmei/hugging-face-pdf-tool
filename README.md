# Hugging Face PDF Tool

![Hugging Face Logo](https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo.png?download=true)

Hugging Face PDF Tool is a lightweight web application that allows users to summarize PDF documents or ask specific questions about their content. The application leverages Hugging Face's state-of-the-art transformer models to provide accurate and efficient natural language processing directly on your PDF files.

## Project Structure

The project is divided into a FastAPI backend and a simple HTML frontend:

- **Backend (`main.py` & `hugging_face_utils.py`)**: A FastAPI server that handles requests for PDF summarization and question-answering. It uses `pypdf` for text extraction and `transformers` for processing.
- **Frontend (`Frontend/index.html`)**: A basic, user-friendly interface for uploading PDF files and entering questions.
- **Utilities (`hugging_face_utils.py`)**: Contains the core logic for reading PDFs and interacting with Hugging Face models (`Falconsai/text_summarization` and `distilbert-base-uncased`).

## Prerequisites

- Python 3.8+
- [Pip](https://pip.pypa.io/en/stable/installation/)

## Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd hugging-face-pdf-tool
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Backend:**
   Start the FastAPI server using Uvicorn:
   ```bash
   python main.py
   ```
   The backend will be running at `http://localhost:8000`.

4. **Open the Frontend:**
   Simply open `Frontend/index.html` in your preferred web browser.

## How to Use

1. **Summarize a PDF**: Select a PDF file and click "Summarize". The backend will extract the text and return a concise summary.
2. **Ask a Question**: Select a PDF file, type your question in the text box, and click "Ask". The tool will find the most relevant answer within the document.

## License

[MIT](LICENSE)
