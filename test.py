import json


class StandardResponseBody:

    def __init__(self, status, message, data = None):
        self.status = status
        self.message = message
        self.data = data

    def to_json(self):
        return json.dumps(self.__dict__)


S = StandardResponseBody(200, "Success")
print(S.to_json())