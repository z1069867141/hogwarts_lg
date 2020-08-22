import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo1:
    def setup_method(self, method):
        # option = Options()
        # option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db = shelve.open("../mydb/logincookies")
        cookies = db["cookie"]
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # myclass = self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").text
        # assert "添加成员" == myclass
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("C:/Users/Akien/Desktop/lagou_study/【测试工程师】三期学习计划(2)(1).xlsx")
        assert "【测试工程师】三期学习计划(2)(1).xlsx" == self.driver.find_element(By.ID, "upload_file_name").text