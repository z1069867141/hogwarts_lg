from test_selenium.test_project.page.add_member_page import AddMember
from test_selenium.test_project.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):
        return AddMember(self.driver)