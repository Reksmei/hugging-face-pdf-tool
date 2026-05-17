from pypdf import PdfReader
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import os 

def read_pdf(file_path: str):
    '''
    Reads a pdf file, page by page and extracts the text for a Hugging Face model to use.
    Args: 
        file_path(str): The path to the pdf file.
        
    Returns: 
        str: The text extracted from the pdf file.
    '''
    pdf = PdfReader(file_path)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text 

def summarize_pdf(file_path:str):
    '''
    Summarizes a pdf file using a lightweight Hugging Face model.
    Args: 
        file_path(str): The path to the pdf file.
        
    Returns: 
        str: The summary of the pdf file.
    '''
    text = read_pdf(file_path)
    tokenizer = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")
    summarizer = pipeline(
        task="text-summarization",
        model=model,
        tokenizer=tokenizer
    )
    return summarizer(text)

def question_pdf(file_path: str, question: str):
    '''
    Answers a user's question about an uploaded pdf file using a lightweight Hugging Face model.
    Args: 
        file_path(str): The path to the pdf file.
        question(str): The question to ask about the pdf file.
        
    Returns: 
        str: The answer to the question.
    '''
    text=read_pdf(file_path)
    questioner=pipeline(
        task="question-answering",
        model="distilbert/distilbert-base-uncased"
    )
    answer = questioner(question=question, context=text)
    return answer["answer"]
