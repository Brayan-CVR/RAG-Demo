from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_splitter(
    chunk_size: int = 2000, chunk_overlap: int = 500
) -> RecursiveCharacterTextSplitter:
    """Creates and configures a recursive character text splitter for document processing.

    This splitter hierarchically divides text using provided separators while maintaining
    consistent chunk sizes according to the specified parameters.

    Args:
        chunk_size (int, optional): Maximum desired size for each chunk (in characters). Default: 2000.
        chunk_overlap (int, optional): Overlap between consecutive chunks (in characters). Default: 500.

    Returns:
        RecursiveCharacterTextSplitter: Configured splitter instance ready for use.

    Example:
        >>> splitter = get_splitter(chunk_size=1000, chunk_overlap=200)
        >>> documents = splitter.split_documents([my_doc])

    Note:
        - Uses len() as default length function. Consider using a tokenizer for LLM-specific applications.
        - Default separators: ["\n\n", "\n", ".", " "]
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,  # Usar len() o tokenizer específico
        separators=["\n\n", "\n", ".", " "],
    )
    return text_splitter


def split_document(text_splitter: RecursiveCharacterTextSplitter, doc: list) -> list:
    """Splits a document or document list into chunks using the provided text splitter.

    Args:
        text_splitter (RecursiveCharacterTextSplitter): Preconfigured text splitter instance.
        doc (list): List of documents to split (typically LangChain Document objects).

    Returns:
        list: List of split documents where each element represents a text chunk.

    Example:
        >>> splitter = get_splitter()
        >>> chunks = split_document(splitter, my_documents)
        >>> print(f"Generated {len(chunks)} chunks")

    Note:
        - Actual chunk sizes may vary slightly from configured chunk_size
        - Original metadata is preserved in each generated chunk
        - For optimal RAG performance, tune chunk_size to your specific embedding model
    """
    split_doc = text_splitter.split_documents(doc)
    return split_doc
