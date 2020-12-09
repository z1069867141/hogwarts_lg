from selenium.webdriver.common.by import By

from test_selenium.test_weixing_demo.base_page import BasePage
from test_selenium.test_weixing_demo.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"  # 子类会覆盖父类url

    def go_to_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register()

    def go_to_login(self):
        pass