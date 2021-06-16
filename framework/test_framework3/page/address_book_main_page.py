from selenium.webdriver.common.by import By

from test_selenium.homework.page.AddApartmentPage import AddMemberPage
from test_selenium.homework.page.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, url):
        self._url = url

    def go_to_add_apartment(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddMemberPage(self.driver)
