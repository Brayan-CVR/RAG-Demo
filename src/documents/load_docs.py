import os
from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf_doc(doc_path: str) -> list:
    """Loads a PDF document and extracts its content as a list of document objects.

    This function uses PyMuPDFLoader from langchain_community to load and parse
    the content of a PDF file, including text and basic metadata (such as page numbers).

    Args:
        doc_path (str): Absolute or relative path to the PDF file to be loaded.

    Returns:
        list: List of documents (typically LangChain Document objects) where each element
              represents a PDF page with its content and metadata.

    Raises:
        FileNotFoundError: If the specified file in doc_path doesn't exist.

    Example:
        >>> documents = load_pdf_doc("report.pdf")
        >>> print(f"Loaded {len(documents)} pages")
        >>> print(documents[0].page_content)  # Content of first page

    Note:
        - The PDF must be accessible and have read permissions.
        - PyMuPDFLoader extracts text but doesn't preserve complex formatting
          (tables, images as text).
    """
    if not os.path.exists(doc_path):
        raise FileNotFoundError(f"El archivo no existe: {doc_path}")

    loader = PyMuPDFLoader(doc_path)
    doc_pdf = loader.load()
    return doc_pdf
