import time

from selenium.webdriver.common.by import By

from testing.base import Base


class Testwindow(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".guide-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".s-top-login-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".pass-reglink").click()
        windows = self.driver.window_handles
        print(windows)
        self.driver.switch_to_window(windows[1])
        self.driver.find_element(By.CSS_SELECTOR, "#TANGRAM__PSP_4__userName").send_keys("z1069867141234321")
        self.driver.find_element(By.CSS_SELECTOR, "#TANGRAM__PSP_4__phone").send_keys("z54821348123")
        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.CSS_SELECTOR, "[title='用户名登录']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#TANGRAM__PSP_11__userName").send_keys("asdoijdisfo")
        self.driver.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_11__password").send_keys("sdioajfiodsj")