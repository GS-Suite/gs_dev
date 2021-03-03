from responses.standard_response_body import StandardResponseBody


class DashboardResponseBody(StandardResponseBody):

    def __init__(self, success, message, user_data = None):
        super().__init__(success, message)
        
        self.data = {
            "first_name": user_data.first_name,
            "last_name": user_data.last_name, 
            "username": user_data.username,
            "email": user_data.email
        }   

        self.data["enrolled"] = []
        self.data["classrooms"] = []
