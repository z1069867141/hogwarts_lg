from selenium.webdriver.common.by import By

from framework.test_framework2.base_page import BasePage


class demo(BasePage):
    _search_button = (By.ID, "home_search")

    # todo: po的数据驱动
    def login(self, username, password):
        pass

    def search(self, keyword):
        self.find(self._search_button).click()
        return self
