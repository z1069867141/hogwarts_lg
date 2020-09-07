from selenium.webdriver.common.by import By

from test_framework.base_page import BasePage


class DemoPage(BasePage):
    _search_button = (By.ID, 'home_search')

    #todo: po的数据驱动
    def login(self):
        pass

    def forget_password(self):
        pass

    def search(self, keyword):
        self.po_run('search')
        # self.find(self._search_button).click()
        return self