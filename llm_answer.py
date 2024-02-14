"""This class implements the ConversationalRetrievalChain to answer the questions using Google's PaLM 2 LLM"""
from langchain.chains import ConversationalRetrievalChain
#fucntion to fetch the answer from chromadb using PaLM 2
def fetch_answer(question, llm, db, chat_history):
    """Returns the answer of the given question from ChromaDB using PaLM 2 LLM"""
    #To create a conversational question-answering chain
    qa_chain = ConversationalRetrievalChain.from_llm(llm, db.as_retriever(),verbose=False,return_source_documents=True)
    #Store the answer after fetching it from the vector database chromadb
    result =  qa_chain.invoke({"question": question, "chat_history": chat_history})
    #stor the answer in chat history
    chat_history.append((question, result["answer"]))
    # Return the content of the most relevant document
    if result:
        return result["answer"] #return the answer fetched from the vector database
    return "No relevant information found." #return this statement when no relevant information is fetched from the database
#End of the File 