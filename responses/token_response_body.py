from responses.standard_response_body import StandardResponseBody


class TokenResponseBody(StandardResponseBody):

    def __init__(self, success, message, data = None):
        super().__init__(success, message)
        if data:
            self.data = {
                "token": data
            }