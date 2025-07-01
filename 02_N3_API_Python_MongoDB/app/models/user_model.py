from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Compra(BaseModel):
    produto_id: str
    descricao: str
    valor: float
    data_compra: str

class Endereco(BaseModel):
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cep: str

class Usuario(BaseModel):
    nome_completo: str
    email: str
    telefone: str
    data_nascimento: str
    endereco: Endereco
    data_cadastro: str
    ativo: bool
    tags: List[str]
    historico_compras: List[Compra]
