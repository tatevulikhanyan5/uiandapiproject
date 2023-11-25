from histories_project.POM.tests.base_test import BaseTest


class TestTopics(BaseTest):

    def test_assert_topics_page_info(self):
        self.homepage.click_on_christmas_start_link()
        self.assert_topic_data()


