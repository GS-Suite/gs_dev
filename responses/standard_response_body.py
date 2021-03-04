


from starlette.responses import JSONResponse


class StandardResponseBody:
    
    def __init__(self, success, message, token = None, data = None):
        self.success = success
        self.message = message

        if token:
            self.token = token
        
        if data:
            self.data = data
        