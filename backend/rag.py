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
        n_results=1,
        include=["documents", "distances"]
    )

    if not resultados["documents"]:
        return None

    distancia = resultados["distances"][0][0]

    print("DISTANCIA:", distancia)

    # Ajustar este valor según las pruebas
    if distancia > 1.0:
        return None

    return resultados["documents"][0][0]