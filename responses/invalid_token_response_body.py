from fastapi import HTTPException

class InvalidTokenResponseBody(HTTPException):
    
    def __init__(self):
        self.status_code = 200
        self.detail = {
            "success": False,
            "message": "Invalid token or non-existent user"
        }
        