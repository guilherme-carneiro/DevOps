from typing import Union

from fastapi import FastAPI

app = FastAPI()

#inicio
@app.get("/")
def read_root():
    return {"Hello": "World"}

#teste 02
@app.get("/teste")
def teste_1():
    return {"Mensagem": "Teste 02 para aprender o processo"}

# Rota para calcular a média de 5 números
@app.post("/calcular_media/")
def calcular_media(numeros: List[float]):
    if len(numeros) != 5:
        return {"Erro": "Você deve fornecer exatamente 5 números."}
    
    media = sum(numeros) / len(numeros)
    return {"Média": media}