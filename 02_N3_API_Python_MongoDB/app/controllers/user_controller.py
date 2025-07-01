from app.database.connection import collection
from bson import ObjectId

def serializar_documento(doc):
    doc["_id"] = str(doc["_id"])
    return doc

def cadastrar_usuario(data):
    return collection.insert_one(data)

def pesquisar_por_nome(nome):
    resultados = collection.find({"nome_completo": {"$regex": nome, "$options": "i"}})
    return [serializar_documento(doc) for doc in resultados]

def pesquisar_por_rua(rua):
    resultados = collection.find({"endereco.rua": {"$regex": rua, "$options": "i"}})
    return [serializar_documento(doc) for doc in resultados]

def pesquisar_por_produto(produto):
    resultados = collection.find({"historico_compras.descricao": {"$regex": produto, "$options": "i"}})
    return [serializar_documento(doc) for doc in resultados]
