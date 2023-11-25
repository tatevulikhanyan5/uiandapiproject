class Endpoints:

    base_url = "https://www.history.com/"
    topics_url = "https://www.history.com/topics"
    reset_pass_url = "https://api.loginradius.com/identity/v2/auth/password?resetPasswordUrl=https%3A%2F%2Fwww.history.com%2Fprofile%2Freset-password&emailTemplate=history-forgotpassword&ApiKey=b7f9668b-0c70-4c52-a21f-f6990609d886"


    def get_topics(self):
        get_topics_url = self.base_url + "editorial/_next/data/UVVwyWLpURTFcD87gpRVi/en/topics.json?path=topics"
        return get_topics_url

