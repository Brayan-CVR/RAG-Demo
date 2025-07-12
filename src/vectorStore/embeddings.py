from langchain_community.embeddings.fastembed import FastEmbedEmbeddings


# "sentence-transformers/all-MiniLM-L6-v2"
def get_embedding_model(model_name: str) -> FastEmbedEmbeddings:
    embed_model = FastEmbedEmbeddings(model_name=model_name)
    return embed_model
