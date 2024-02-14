# Generative AI Final Assignment
## Building a PDF question-and-answer application with LangChain, Google PaLM 2, and Chroma Vector Database.
This README provides an overview of the project structure and instructions for setting up and running the Q&A system based on PDF documents using FastAPI, Chroma Vector Database, LangChain, and Google PaLM 2.

### Project Structure
The project structure consists of the following files:

1. `config.py`: Configuration file containing constants and configurations for the application.
2. `chroma_db.py`: Module for interacting with the Chroma Vector Database.
3. `llm_answer.py`: Module for generating answers using LangChain and Google PaLM 2.
4. `pdf_handler.py`: Module for handling PDF documents, segmenting text, and generating embeddings.
5. `main.py`: Main FastAPI application file containing API endpoints.
6. `requirements.txt`: File listing all required dependencies.

### Installation
To set up the project environment, follow these steps:

Ensure you have Python 3.7 or higher installed on your system.
This project has been run on python version 3.11.

Create a virtual environment using conda or venv.
```bash
conda create -n <environment name> python=3.11
```
Clone the repository or download the project files.
Navigate to the project directory.
Install the dependencies listed in requirements.txt using pip:
```bash
pip install -r requirements.txt
```
### Running the Application
To run the Q&A system, execute the following command:

```bash
uvicorn main:app
```

or 

Type `python main.py` in the bash/powershell/cmd terminal.

This will start the FastAPI application.

## API Endpoints
The application provides the following API endpoints:

### 1. PDF Upload Endpoint
1. Method: `POST`

2. URL: `/upload/`

3. Parameters: `pdf_path` (Path to the PDF file) and `pdf_name` (Name of the PDF file)

4. Description: 
Uploads a PDF document to the application. The document is segmented into smaller chunks for processing. Returns a success message if the document is successfully converted to embeddings and saved to the Chroma Db.

### 2. Q&A Endpoint

1. Method: `GET`

2. URL: `/query/`

3. Parameters: `question` (User's question) and `pdf_name` (Name of the PDF file)

4. Description: 
Accepts a user's question and the name of the PDF document. Queries the Chroma Vector Database using the user's question and retrieves relevant segments of the PDF documents based on the search results. Returns the answer to the user's question using LangChain and Google PaLM 2.

## Testing

We can test the application by using a set of questions from PDF documents to verify its functionality. We can test each endpoint using SwaggerUI on `127.0.0.1/docs`.

## Conclusion
This README provides an overview of the Q&A system based on PDF documents. Follow the installation instructions to set up the environment and run the application. For further details, refer to the code documentation and comments within each module.