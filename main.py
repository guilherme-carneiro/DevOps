from typing import Union
from typing import List
from fastapi import FastAPI

app = FastAPI()

#inicio
@app.get("/")
def read_root():
    return {"Hello": "World"}