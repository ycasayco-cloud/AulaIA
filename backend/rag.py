import chromadb

client = chromadb.PersistentClient(path="./database/chroma")

collection = client.get_or_create_collection("curso")

def guardar_documento(texto, nombre):

    collection.add(
        documents=[texto],
        ids=[nombre]
    )

def buscar_contexto(pregunta):

    resultados = collection.query(
        query_texts=[pregunta],
        n_results=1
    )

    return resultados["documents"][0][0]