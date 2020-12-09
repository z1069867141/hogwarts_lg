import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbuttom(self):
        self.driver.get("https://www.baidu.com")
        text_element = self.driver.find_element(By.CSS_SELECTOR, '.s_ipt')
        search_element = self.driver.find_element(By.CSS_SELECTOR, '#su')

        text_element.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(search_element)
        action.scroll_from_element(search_element,0,10000)
        action.perform()
        time.sleep(5)