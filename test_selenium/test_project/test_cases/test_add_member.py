from test_selenium.test_project.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        self.main = MainPage()
        self.main.go_to_add_member()
        self.main.go_to_contact().go_to_add_member().add_member()

# if __name__ == "__main__":
#