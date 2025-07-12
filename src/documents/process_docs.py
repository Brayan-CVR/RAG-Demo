from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_splitter(
    chunk_size: int = 2000, chunk_overlap: int = 500
) -> RecursiveCharacterTextSplitter:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,  # Usar len() o tokenizer específico
        separators=["\n\n", "\n", ".", " "],
    )
    return text_splitter


def split_document(text_splitter: RecursiveCharacterTextSplitter, doc: list) -> list:
    split_doc = text_splitter.split_documents(doc)
    return split_doc
