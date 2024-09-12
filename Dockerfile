FROM python:3

WORKDIR /usr/src/app

# Copiar e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta 8000 para acessar a API
EXPOSE 8000

# Comando para rodar o Uvicorn e a aplicação FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
