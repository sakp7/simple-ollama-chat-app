# Required Libraries

import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [

    ("system","You are an helpful AI assitant"),
    ("user","Question:{question}")
    ]
    )

# Initializing Ollama
llm=OllamaLLM(model='llama3.1:latest')

# Initializing OutputParser
output_parser=StrOutputParser()

st.title("Simple LLM application with Ollama")
a=st.text_input("enter your query")
chain=prompt|llm|output_parser
if a:
    resp=chain.invoke({'question':a})
    st.write(resp)

