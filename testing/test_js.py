import time

from selenium.webdriver.common.by import By

from testing.base import Base


class Testjs(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(2)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        for code in [
            "return document.title", "return JSON.stringify(performance.timing)"
        ]:
            print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_js_time(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("a.value='2020-12-30'")
        time.sleep(5)
        print(self.driver.execute_script("return a.value"))