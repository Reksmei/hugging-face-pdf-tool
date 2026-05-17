from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn 
import hugging_face_utils 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)


@app.post("/summarize")
def main_summarize(file_path:str):
    return hugging_face_utils.summarize_pdf(file_path)

@app.post("/question")
def main_question(file_path:str, question: str):
    return hugging_face_utils.question_pdf(file_path, question)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)