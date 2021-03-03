from responses.standard_response_body import StandardResponseBody


class ClassroomsResponseBody(StandardResponseBody):

    def __init__(self, success, message, cls = None):
        super().__init__(success, message)
        
        self.data = {
            "classroom": {
                "name": cls.name,
                "uid": cls.uid
            }
        }