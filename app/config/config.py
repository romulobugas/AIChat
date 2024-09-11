# app/config/config.py

class Config:
    LLM_API_ENDPOINT = "http://localhost:1234/v1"  # URL do LMStudio
    API_KEY = "lm-studio"  # Chave da API do LMStudio

    @staticmethod
    def get_llm_endpoint():
        return Config.LLM_API_ENDPOINT

    @staticmethod
    def get_api_key():
        return Config.API_KEY
