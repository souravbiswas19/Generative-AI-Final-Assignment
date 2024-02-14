"""Importing the necessary modules"""
import os
from fastapi import FastAPI, HTTPException, status
from langchain_community.embeddings import GooglePalmEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from config import fetch_google_key
from config import chroma_instances
from pdf_handler import process_pdf
from chroma_db import upload_to_chromadb
from llm_answer import fetch_answer
google_api_key=fetch_google_key()

#Initializaing the Google PaLM 2 LLM. text-bison-001 is the name of the model
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=google_api_key)
#Temperature of the LLM model is set. 
#A lower temperature value makes the AI's responses more focused and deterministic.
llm.temperature = 0.1
#To store the history of the searched questions and it's answers
chat_history=[]
#Initializing FastAPI
app = FastAPI()
#POST api endpoint to accept the path and name of the pdf file and uplaod it to chromadb Database.
@app.post("/upload/", status_code=status.HTTP_202_ACCEPTED)
async def upload_file(pdf_path: str = None, pdf_name: str = None):
    """Function to upload a file"""
    #joining the file path and pdf name to fetch it from the specified location
    file_path=os.path.join(pdf_path, pdf_name)
    #Handling the Exceptions if the file exists in the specified directory or not
    try:
        # Load the PDF document using file_path from process_pdf from pdf_handler.py
        docs=process_pdf(file_path)
        #Initializing GooglePalmEmbeddings function
        embeddings = GooglePalmEmbeddings(google_api_key=google_api_key)
        #collection name is stored as the name of the pdf only without '.pdf' extension
        coll_name = pdf_name[:-4]
        #Creating the chromaDB folder to store the embeddings locally.
        db=upload_to_chromadb(docs, embeddings, coll_name)
        # Store the Chroma instance in the dictionary to fetch them during retrieval when we are 
        chroma_instances[coll_name] = db
        # Optionally, you can return some information
        return {"message": f"File '{pdf_name}' uploaded successfully and processed with collection name '{coll_name}'."}
    #Exception encountered when the file doesn't exist at that paricular location
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    
#GET API endpoint to search the question from the chromaDB database using Langchain 
@app.get("/query/", status_code=status.HTTP_302_FOUND)
async def query_pdf(pdf_name: str, question: str):
    """Query the function version."""
    try:
        # Check if the specified PDF exists in the dictionary
        pdf_name=pdf_name[:-4]
        if pdf_name not in chroma_instances:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"PDF '{pdf_name}' not found in the database")
        # Retrieve the Chroma instance for the specified PDF
        db = chroma_instances[pdf_name]
        #PaLM 2 Integration
        ans=fetch_answer(question, llm, db, chat_history)
        #returns the answer after successful search from the pdf
        return {"answer": ans}
    #Exception encountered if the pdf does not exist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e

#checks whether the current script is being run as the main program
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
#End of file