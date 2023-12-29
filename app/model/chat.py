"""Model module that contains the code relevant to the model we want to query.

Ideally we would use Olama for a locally running quantised LLama-2
assuming we have  sufficient RAM/VRAM.
"""
import os

import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from app.utils.fetch_papers import (fetch_papers, load_papers_from_json,
                                    save_papers_to_json)


@st.cache_resource
def chain_workflow():
    llm_name = "gpt-3.5-turbo"

    # persist_directory
    persist_directory = "vector_index/"

    # Load OpenAI embedding model
    embeddings = OpenAIEmbeddings()

    # Check if the file exists
    if not os.path.exists("vector_index/chroma.sqlite3"):
        # If it doesn't exist, create it

        documents = fetch_papers()

        persist_directory = "vector_index/"

        vectordb = Chroma.from_documents(documents=documents,
                                         embedding=embeddings,
                                         persist_directory=persist_directory)

        vectordb.persist()
        print(
            "Vectorstore created and saved successfully, The 'chroma.sqlite3' file has been created."
        )
    else:
        # if vectorstore already exist, just call it
        vectordb = Chroma(persist_directory=persist_directory,
                          embedding_function=embeddings)

    # Load OpenAI chat model
    llm = ChatOpenAI(temperature=0)

    # specify a retrieval to retrieve relevant splits or documents
    compressor = LLMChainExtractor.from_llm(llm)
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=vectordb.as_retriever(search_type="mmr",
                                             search_kwargs={"k": 3}),
    )

    # Create memory 'chat_history'
    memory = ConversationBufferWindowMemory(k=3, memory_key="chat_history")

    # create a chatbot chain
    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model=llm_name, temperature=0),
        chain_type="map_reduce",
        retriever=compression_retriever,
        memory=memory,
        get_chat_history=lambda h: h,
        verbose=True,
    )

    return qa
