from test_selenium.test_project.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        self.main = MainPage()
        self.main.go_to_add_member().add_member()

    def test_contact_add_member(self):
        self.main.go_to_contact().go_to_add_member().add_member()

    def teardown(self):
        self.main.driver.quit()