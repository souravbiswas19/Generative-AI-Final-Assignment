"""This file implements the extraction of pdf content from pdf file and returns them as Document objects"""
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
#fucntion to accept the file name and return a Document object
def process_pdf(file_path):
    """PyPDFLoader has been used to load the pdf from the specified location of the path mentioned"""
    loader = PyPDFLoader(file_path)
    #file converted to document
    documents = loader.load()
    #The whole document is split into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    return docs #return the document object
#End of file 