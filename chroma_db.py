"""Importing the necessary modules"""
import os
from langchain_community.vectorstores import Chroma
#fucntion to upload the document by using GooglePaLMEmbedding to chromaDB
def upload_to_chromadb(docs, embeddings, coll_name):
    """Upload the document to chromaDB"""
    #create a local database directory
    db_dir = os.path.join("", "ChromaDB")
    os.makedirs(db_dir, exist_ok=True)
    #creating the chromaDB folders with pdf file name
    db_path = os.path.join(db_dir, f"{coll_name}.db")
    #adding embedding and text data to the chromaDB folder with collection name as pdf name
    db = Chroma.from_documents(docs, embeddings, collection_name=coll_name, persist_directory=db_path)
    return db
#End of file