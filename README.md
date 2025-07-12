# RAG-Demo

![Python](https://img.shields.io/badge/python-3.10%2B-blue) 
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen)](https://brayan-cvr.github.io/RAG-Demo/) 
![LangChain](https://img.shields.io/badge/LangChain-0.3.x-orange) 
![Ollama](https://img.shields.io/badge/Ollama-LLM_Integration-green)

Python **Retrieval-Augmented Generation (RAG)** project for document processing with local or remote LLM models. Includes text extraction, embeddings, vector stores, and contextual answer generation.

## 📚 Documentation

Full documentation hosted on GitHub Pages:  
🔗 [https://brayan-cvr.github.io/RAG-Demo/](https://brayan-cvr.github.io/RAG-Demo/)

## 🚀 Key Features

- **Document processing** (PDF, text) with `PyMuPDF`
- **Fast local embeddings** using `fastembed`
- **Vector storage** with `ChromaDB` (`langchain-chroma`)
- **Ollama integration** to run free LLM models locally (e.g., Llama3, Mistral)
- **Modular pipeline** with `LangChain` for customizable RAG
- Automatic documentation with `Sphinx` and `Furo` theme

## 📦 Libraries Used

```python
dependencies = [
    "langchain>=0.3.26",
    "langchain-community>=0.3.27",
    "langchain-chroma>=0.2.4",
    "pymupdf>=1.26.3",  # PDF processing
    "fastembed>=0.7.1",  # Fast embeddings
    "langchain-ollama>=0.3.4",  # Ollama connection
    "sphinx>=8.2.3",    # Docs
    "myst-parser>=4.0.1",
    "furo>=2024.8.6",   # Docs theme
    "pytest>=8.4.1"     # Testing
]