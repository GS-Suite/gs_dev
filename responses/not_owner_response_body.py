from fastapi import HTTPException


class NotOwnerResponseBody(HTTPException):
    def __init__(self, token):
        self.status_code = 200
        self.detail = {
            "success": False,
            "message": 'You are not the owner of the classroom',
            "token": token
        }
        