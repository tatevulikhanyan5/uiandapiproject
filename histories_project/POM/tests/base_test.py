import pytest

from histories_project.api.rest_requests import Rest

@pytest.mark.usefixtures('get_driver')
class BaseTest(Rest):

    def get_topics_data(self):
        return self.make_get_request(self.endpoints.get_topics())

    def assert_topic_data(self):
        data_dict = self.get_topics_data()
        link_of_topics = data_dict["pageProps"]["post"]["link"]
        assert link_of_topics == self.endpoints.topics_url

    def reset_pass_via_registrated_email(self, email: str = "", status_code: int = 200):
        url = self.endpoints.reset_pass_url
        json_body = self.jsonbody.create_reset_password_json(email)
        return self.make_post_request_success_status(url=url, json_body=json_body, status_code=status_code)

    def reset_pass_via_non_registrated_email(self, email: str = "", status_code: int = 403):
        url = self.endpoints.reset_pass_url
        json_body = self.jsonbody.create_reset_password_json(email)
        return self.make_post_request_all_statuses(url=url, json_body=json_body, status_code=status_code)

