# app/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv
from app.controllers.langchain_controller import LangChainController
from app.views.response_format import ResponseFormatter

# Carrega as variáveis do arquivo .env
load_dotenv()

app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especifique a origem do front-end, ex: ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

controller = LangChainController()

@app.get("/")
def read_root():
    return {"message": "API está funcionando na porta configurada"}

# Endpoint /query para processar o prompt
@app.post("/query")
async def query_llm(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    # Chama o controlador para processar a requisição
    response = controller.handle_request(prompt)
    
    # Formata e retorna a resposta
    return ResponseFormatter.format_response(response)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    print(f"Iniciando o servidor na porta {port}")
    
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)
