from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


def __get_prompt_template_base__() -> PromptTemplate:
    custom_prompt_template = """
    Eres un asistente experto en análisis de políticas públicas de seguridad de la información y privacidad. 
    Tienes acceso a fragmentos del documento oficial llamado "Plan Estratégico de Seguridad y Privacidad de la Información 2024".

    Este plan fue diseñado con base en estándares internacionales, evaluaciones de riesgo, marcos legales y buenas prácticas para garantizar la protección de datos y sistemas críticos. 
    Contiene diagnósticos, objetivos estratégicos, controles de seguridad y protocolos de actuación.

    **Instrucciones:**
    1. Usa ÚNICAMENTE la información proporcionada en los fragmentos del documento para responder.
    2. Sé preciso y técnico en respuestas relacionadas con ciberseguridad y privacidad.
    3. Si la pregunta requiere información externa o no está en el documento, responde: 
    “No se encuentra información suficiente en el documento para responder con certeza”.

    Pregunta: {question}

    Fragmentos del documento:
    {context}
    """
    prompt = PromptTemplate(
        template=custom_prompt_template, input_variables=["context", "question"]
    )

    return prompt


def get_qa_chain(llm, retriever):
    prompt = __get_prompt_template_base__()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )

    return qa
