import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Output parser,ollala

prompt=ChatPromptTemplate.from_messages(
    [

    ("system","You are an helpful assitant"),
    ("user","Question:{question}")
    ]
    )
llm=OllamaLLM(model='llama3.1:latest')

st.title("Simple LLM application with Ollama")
a=st.text_input("enter your query")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if a:
    resp=chain.invoke({'question':a})
    st.write(resp)


