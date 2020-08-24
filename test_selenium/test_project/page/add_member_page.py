from selenium.webdriver.common.by import By
from test_selenium.test_project.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.driver.find_element(By.ID, 'username').send_keys("username")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("Akien")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("18018161651")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()