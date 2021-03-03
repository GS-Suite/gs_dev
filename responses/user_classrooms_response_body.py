from responses.standard_response_body import StandardResponseBody


class UserClassroomsResponseBody(StandardResponseBody):

    def __init__(self, success, message, classrooms = None):
        super().__init__(success, message)
        
        self.data = {
            "classrooms": [
                {
                    "name": i.name,
                    "uid": i.uid
                } for i in classrooms
            ]
        }