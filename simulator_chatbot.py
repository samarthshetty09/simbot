import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile

from dotenv import load_dotenv
import os


load_dotenv(override=True)



open_ai_api_key = os.getenv("OPEN_AI_API_KEY")

loader = CSVLoader(file_path='simulator_data.csv')
data = loader.load()



embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(data,embeddings)
chain = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo',openai_api_key=open_ai_api_key),retriever=vectorstore.as_retriever())




def query_bot(query):
    response = chain({"question": query,"chat_history":st.session_state['history']})
    st.session_state.history.append(response['answer'])
    return response['answer']




if 'history' not in st.session_state:
    st.session_state.history = []


if 'bot' not in st.session_state.keys():
    print("Generating")
    st.session_state.bot = ["Hello! How can I help you today?"]



if 'past' not in st.session_state:
    st.session_state.past = ['Hey! How can I help you today?']



response_container = st.container()

container = st.container()


with container:
    with st.form(key='simulator_form',clear_on_submit=True):
        query = st.text_input("Query:",placeholder='Enter your query here:',key='input')
        submit_button = st.form_submit_button(label='Submit')


    if submit_button and query:
        output = query_bot(query)
        st.session_state.past.append(query)
        st.session_state.bot.append(output)  

if st.session_state.bot:
    with response_container:
        for i in range(len(st.session_state.bot)):
            message(st.session_state.past[i],is_user=True,key=str(i) + '_user',avatar_style='big-smile')
            message(st.session_state.bot[i],key=str(i),avatar_style='thumbs')