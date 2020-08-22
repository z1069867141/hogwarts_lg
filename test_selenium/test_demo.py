
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo1:
    def setup_method(self, method):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo1(self):
        self.driver.get("https://ceshiren.com")
        self.driver.set_window_size(1536, 960)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        # 断言
        myclass = self.driver.find_element(By.LINK_TEXT, "所有分类").get_attribute("class")
        assert "active" == myclass