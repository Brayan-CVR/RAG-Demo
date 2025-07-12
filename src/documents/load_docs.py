import os
from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf_doc(doc_path: str) -> list:
    if not os.path.exists(doc_path):
        raise FileNotFoundError(f"El archivo no existe: {doc_path}")

    loader = PyMuPDFLoader(doc_path)
    doc_pdf = loader.load()
    return doc_pdf
