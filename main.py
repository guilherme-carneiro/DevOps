from fastapi import FastAPI, Query
from typing import Union

app = FastAPI()

# Rota aula para se basear
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Rota para a calculadora
@app.get("/calculadora")
def calcular(operacao: str, num1: float = Query(...), num2: float = Query(...)):
    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subtracao":
        resultado = num1 - num2
    elif operacao == "multiplicacao":
        resultado = num1 * num2
    elif operacao == "divisao":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return {"Erro": "Divisão por zero não é permitida"}
    else:
        return {"Erro": "Operação inválida. Use: soma, subtracao, multiplicacao ou divisao"}

    return {"resultado": resultado}
