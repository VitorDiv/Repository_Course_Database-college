from fastapi import FastAPI
from app.routes import user_routes  # importe o módulo onde estão suas rotas

app = FastAPI()

app.include_router(user_routes.router)  # inclua o router aqui

@app.get("/")
def root():
    return {"message": "Olá! API funcionando"}
