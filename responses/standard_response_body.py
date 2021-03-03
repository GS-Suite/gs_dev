


class StandardResponseBody:
    
    def __init__(self, success, message, data = None):
        self.success = success
        self.message = message

        if data:
            self.data = data