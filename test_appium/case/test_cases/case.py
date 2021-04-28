from test_appium.case.page.app import App
from test_appium.case.page.mainpage import mainpage

class Testcase:
    def setup(self):
        self.driver = App().start()

    def test_case1(self):
        mainpage().click_contact_list()