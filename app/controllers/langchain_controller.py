# app/controllers/langchain_controller.py
from app.services.langchain_service import LangChainService

class LangChainController:
    def __init__(self):
        self.service = LangChainService()

    def handle_request(self, prompt: str) -> dict:
        return self.service.process_prompt(prompt)
