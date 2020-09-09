from test_framework.base_page import BasePage


class LoginPage(BasePage):
    def login_by_password(self, username, password):
        self.po_run("login_by_password", username=username, password=password)
