class JsonBuilders:

    def create_reset_password_json(self, email: str = ""):
        return {"email" : f"{email}"}



