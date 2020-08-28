from selenium.webdriver.common.by import By
from test_selenium.homework.page.base_page import BasePage

class AddMemberPage(BasePage):
    def add_apartment(self):
        self.find(By.CSS_SELECTOR, "[name=name]").send_keys("测试部门")
        self.find(By.CSS_SELECTOR, ".qui_dialog_body [class='qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list']").click()
        self.find(By.XPATH, "//div[@class='jstree jstree-8 jstree-default']//a[@id='1688853785095996_anchor']").click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_foot .ww_btn_Blue").click()
        text = self.find(By.CSS_SELECTOR, "#js_tips").text
        return text