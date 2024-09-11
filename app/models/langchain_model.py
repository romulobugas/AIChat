# app/models/langchain_model.py
import requests
from app.config.config import Config

class LangChainModel:
    def __init__(self):
        self.endpoint = Config.get_llm_endpoint()
        self.api_key = Config.get_api_key()

    def query_llmstudio(self, prompt: str) -> dict:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
            "messages": [
                {
                    "role": "system",
                    "content": "This is a chat between a user and an assistant. The assistant is helping the user to answer the question."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 1000
        }

        try:
            response = requests.post(f"{self.endpoint}/chat/completions", json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
