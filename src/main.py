#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Custom imports
from initialization.system_information import print_python_details
from initialization.logger_control import start_logger, get_logger
from vectorStore.vs import create_vector_store, set_chroma_as_retriever
from vectorStore.embeddings import get_embedding_model
from llm.load_llm import get_ollama_llms
from llm.promp import get_qa_chain

# Star logger
start_logger()
logger = get_logger(__name__)


def main_process(
    generate_vs: bool,
    vs_path: str,
    context_document_path: str,
    collection_name: str,
    embedding_model_name: str,
    chunk_size: int,
    chunk_overlap: int,
    llm_name: str,
    show_metadata:bool
) -> bool:
    """Orchestrates the main RAG (Retrieval-Augmented Generation) pipeline.

    This function handles:
    - Vector Store creation (when needed)
    - Embedding model loading
    - Retriever configuration 
    - LLM model initialization
    - Interactive query execution

    Args:
        generate_vs (bool): If True, creates new Vector Store. If False, uses existing one.
        vs_path (str): Path to store/create the Vector Store.
        context_document_path (str): PDF document path for embeddings (if generate_vs=True).
        collection_name (str): ChromaDB collection name.
        embedding_model_name (str): Embedding model name (e.g., "sentence-transformers/all-MiniLM-L6-v2").
        chunk_size (int): Document chunk size (in tokens).
        chunk_overlap (int): Chunk overlap size (in tokens).
        llm_name (str): LLM model name to load (e.g., "gemma:2b").
        show_metadata (bool): If True, displays metadata of retrieved documents.

    Returns:
        bool: True if execution succeeds, False if any error occurs.

    Raises:
        Exception: Logs critical errors before returning False.

    Example:
        >>> if __name__ == "__main__":
        ...     params = {
        ...         "generate_vs": True,
        ...         "vs_path": "/path/to/vectorstore",
        ...         # ... other parameters ...
        ...     }
        ...     success = main_process(**params)
        ...     print("Success:" if success else "Failed:", success)

    Note:
        - For production use, consider adding input validation
        - ChromaDB persistence depends on vs_path configuration
        - LLM performance depends on proper chunk_size configuration
    """
    try:
        logger.info("Running main process.\n")
        print_python_details()

        if generate_vs:
            logger.info("Generating Vector Store...\n")
            create_vector_store(
                vs_path=vs_path,
                sample_path=context_document_path,
                vs_collection_name=collection_name,
                embedding_model_name=embedding_model_name,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
            )

        embedding_model = get_embedding_model(embedding_model_name)

        retriever = set_chroma_as_retriever(
            embedding_model, vs_path, collection_name, 10
        )

        llm_model = get_ollama_llms(llm_name)

        qa = get_qa_chain(llm_model, retriever)

        q = input("Ingrese su consulta: ")

        response = qa.invoke({"query": q})
        logger.info("----RESPUESTA----: \n" + response["result"] + "\n")

        if show_metadata:
            metadata = []
            for _ in response["source_documents"]:
                metadata.append((_.metadata["page"], _.metadata["file_path"]))

            logger.info(metadata)

        return True
    except Exception as e:
        logger.error(e)
        return False


if __name__ == "__main__":
    # Parameters
    generate_vs = False
    vs_path = "/Users/brayan/Documents/RAG-Demo/src/vectorStore/vs_local"
    context_document_path = "/Users/brayan/Documents/RAG-Demo/src/vectorStore/samples/Cuarto-informe-de-gestion-SEB-firmado-300125.pdf"
    collection_name = "informe_ministerio_de_educacion"
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    chunk_size = 800
    chunk_overlap = 100
    llm_name = "gemma:2b"
    show_metadata = False

    # Start the main execution process
    if main_process(
        generate_vs=generate_vs,
        vs_path=vs_path,
        context_document_path=context_document_path,
        collection_name=collection_name,
        embedding_model_name=embedding_model_name,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        llm_name=llm_name,
        show_metadata = show_metadata
    ):
        logger.info("Successful execution.")
    else:
        logger.error("Failed execution.")
