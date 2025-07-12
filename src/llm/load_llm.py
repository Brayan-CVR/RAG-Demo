from langchain_ollama import OllamaLLM


# "llama3.2"
def get_ollama_llms(model_name):
    llm = OllamaLLM(model=model_name)
    return llm
