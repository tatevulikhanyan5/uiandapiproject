from histories_project.POM.tests.base_test import BaseTest


class TestResetPass(BaseTest):

    def test_reset_pass_via_registered_email(self, email="heheli1741@ipnuc.com"):
        response = self.reset_pass_via_registrated_email(email=email)
        assert response["IsPosted"]==True

    def test_reset_pass_via_non_registered_email(self, email="heheli1741@ipnuc.com"):
        self.reset_pass_via_non_registrated_email(email=email, status_code=403)
