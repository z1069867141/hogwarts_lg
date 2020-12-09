import time

from selenium.webdriver.common.by import By

from testing.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#sttb").click()
        self.driver.find_element(By.CSS_SELECTOR, "#stfile").send_keys("C:\\Users\\v-akienli\\Desktop\\QQ截图20201207194731.png")
        time.sleep(5)