from selenium.webdriver.common.by import By

from framework.test_framework2.base_page import BasePage


class DemoPage(BasePage):
    # _search_button = (By.ID, "home_search")

    # todo: po的数据驱动
    def login(self, username, password):
        pass

    #todo: po的参数化
    def search(self, keyword):
        self.po_run('search', keyword=keyword)
        return self
