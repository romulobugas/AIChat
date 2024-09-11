# app/services/langchain_service.py
from app.models.langchain_model import LangChainModel

class LangChainService:
    def __init__(self):
        self.model = LangChainModel()

    def process_prompt(self, prompt: str) -> dict:
        if not prompt:
            return {"error": "O prompt não pode estar vazio"}
        
        # Interage com o LLMStudio via o modelo
        return self.model.query_llmstudio(prompt)
