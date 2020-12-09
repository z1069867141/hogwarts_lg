import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.CSS_SELECTOR, "[value='click me']")
        element_double_click = self.driver.find_element(By.CSS_SELECTOR, "[value='dbl click me']")
        element_right_click = self.driver.find_element(By.CSS_SELECTOR, "[value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        action.context_click(element_right_click)
        action.perform()

    @pytest.mark.skip
    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com")
        element_move_to = self.driver.find_element(By.CSS_SELECTOR, "#s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(element_move_to)
        action.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element_drag = self.driver.find_element(By.CSS_SELECTOR, "#dragger")
        element_drop = self.driver.find_element(By.CSS_SELECTOR, '.item')

        action = ActionChains(self.driver)
        # action.drag_and_drop(element_drag, element_drop).perform()
        # action.click_and_hold(element_drag).release(element_drop).perform()
        action.click_and_hold(element_drag).move_to_element(element_drop).release().perform()
        time.sleep(3)

    def test_sendkeys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        element_sendkeys = self.driver.find_element(By.CSS_SELECTOR, "[type='textbox']")
        element_sendkeys.click()
        action = ActionChains(self.driver)
        action.send_keys("username")
        action.send_keys(Keys.SPACE).pause(1)  # pause有暂停效果
        action.send_keys("to")
        action.send_keys(Keys.BACK_SPACE)
        action.perform()
        time.sleep(5)