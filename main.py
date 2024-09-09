from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/teste")
def teste_1():
    return {"Mensagem": "Deu errado"}