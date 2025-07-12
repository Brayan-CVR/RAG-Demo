from langchain_chroma import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# Custom libreries
from documents.load_docs import load_pdf_doc
from documents.process_docs import get_splitter
from documents.process_docs import split_document
from vectorStore.embeddings import get_embedding_model


def create_vector_store(
    vs_path: str,
    sample_path: str,
    vs_collection_name: str,
    embedding_model_name: str,
    chunk_size: int,
    chunk_overlap: int,
):
    doc = load_pdf_doc(sample_path)

    text_splitter = get_splitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    split_doc = split_document(text_splitter, doc)

    embedding_model = get_embedding_model(embedding_model_name)

    vs = generate_chroma_vs(
        split_doc, embedding_model, vs_path, vs_collection_name
    )


def generate_chroma_vs(
    docs_list: str,
    embedding_model: FastEmbedEmbeddings,
    persist_directory: str,
    collection_name: str,
) -> Chroma:
    vs = Chroma.from_documents(
        documents=docs_list,
        embedding=embedding_model,
        persist_directory=persist_directory,  # Local mode with in-memory storage only
        collection_name=collection_name
    )

    return vs


def set_chroma_as_retriever(
    embedding_model: FastEmbedEmbeddings,
    persist_directory: str,
    collection_name: str,
    number_of_chunks: int,
):
    vectorstore = Chroma(
        embedding_function=embedding_model,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": number_of_chunks})

    return retriever
