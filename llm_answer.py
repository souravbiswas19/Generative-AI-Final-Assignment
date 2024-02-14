from langchain.chains import ConversationalRetrievalChain

def fetch_answer(question, llm, db, chat_history):
    qa_chain = ConversationalRetrievalChain.from_llm(llm, db.as_retriever(),verbose=False,return_source_documents=True)
    result =  qa_chain.invoke({"question": question, "chat_history": chat_history})
    print("Answer: " + result["answer"])
    chat_history.append((question, result["answer"]))
    # Return the content of the most relevant document
    if result:
        return result["answer"]
    else:
        return "No relevant information found."