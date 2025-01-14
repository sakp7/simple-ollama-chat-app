Simple LLM Application with Ollama**
=====================================

**Project Name:** Simple LLM Application with Ollama
**Project Details:** This project is a simple implementation of a Large Language Model (LLM) application using Ollama and Streamlit.
### Required Libraries

*   `streamlit`: A Python library for building custom web applications.
*   `langchain_ollama`: A Python library for interacting with the Ollama LLM.
*   `langchain_core`: A Python library for building and executing language chains.

### Problems Solved

*   This project solves the problem of building a simple LLM application using Ollama and Streamlit.
*   It demonstrates how to use the `langchain_ollama` library to interact with the Ollama LLM.
*   It shows how to use Streamlit to build a simple web application that takes user input and uses the LLM to generate a response.

### Tech Stack Used

*   **Programming Language:** Python
*   **LLM:** Ollama
*   **Web Framework:** Streamlit
*   **Library:** `langchain_ollama` and `langchain_core`

### Project Implementation

#### Step 1: Importing Libraries

```python
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

*   This code imports the required libraries, including `streamlit`, `langchain_ollama`, and `langchain_core`.

#### Step 2: Initializing Prompt Template

```python
# Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
    ("system","You are an helpful AI assistant"),
    ("user","Question:{question}")
    ]
    )
```

*   This code initializes a prompt template using the `ChatPromptTemplate.from_messages` method.
*   The prompt template is defined as a conversation between a system and a user.

#### Step 3: Initializing Ollama

```python
# Initializing Ollama
llm=OllamaLLM(model='llama3.1:latest')
```

*   This code initializes the Ollama LLM using the `OllamaLLM` class.
*   The `llama3.1:latest` model is used.

#### Step 4: Initializing Output Parser

```python
# Initializing Output Parser
output_parser=StrOutputParser()
```

*   This code initializes an output parser using the `StrOutputParser` class.

#### Step 5: Building the Language Chain

```python
chain=prompt|llm|output_parser
```

*   This code builds a language chain using the `prompt`, `llm`, and `output_parser` components.

#### Step 6: Building the Streamlit Application

```python
st.title("Simple LLM application with Ollama")
a=st.text_input("enter your query")
if a:
    resp=chain.invoke({'question':a})
    st.write(resp)
```

*   This code builds a Streamlit application that takes user input and uses the language chain to generate a response.
*   The response is then displayed to the user.

### Project Deployed Link

The project is deployed on Streamlit Cloud and can be accessed at [https://example.com](https://example.com).

### Project Database Link

The project does not use a database.

### Conclusion

This project demonstrates how to build a simple LLM application using Ollama and Streamlit. It shows how to use the `langchain_ollama` library to interact with the Ollama LLM and how to use Streamlit to build a simple web application.
