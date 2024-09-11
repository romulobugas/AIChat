# app/views/response_format.py

class ResponseFormatter:
    @staticmethod
    def format_response(data: dict) -> dict:
        if "error" in data:
            return {"status": "error", "message": data["error"]}
        return {"status": "success", "response": data}
