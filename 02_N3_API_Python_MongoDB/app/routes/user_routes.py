from fastapi import APIRouter
from app.controllers import user_controller
from app.models.user_model import Usuario
from fastapi import APIRouter, Request
from app.controllers.user_controller import (
    cadastrar_usuario,
    pesquisar_por_nome,
    pesquisar_por_rua,
    pesquisar_por_produto
)

router = APIRouter()

@router.post("/cadastrar")
async def cadastrar(usuario: Usuario):
    data = usuario.dict()
    result = user_controller.cadastrar_usuario(data)
    return {"inserted_id": str(result.inserted_id)}

@router.get("/pesquisar_nome")
def pesquisar_nome(nome: str):
    return pesquisar_por_nome(nome)

@router.get("/pesquisar_rua")
def pesquisar_rua(rua: str):
    return pesquisar_por_rua(rua)

@router.get("/pesquisar_compras")
def pesquisar_compras(produto: str):
    return pesquisar_por_produto(produto)
