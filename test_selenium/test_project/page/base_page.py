from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    url = ""

    def __init__(self, driver_base=None): #driver_base每次调用该父级类型的时候是否有传参数，如果有就跳过配置浏览器
        if driver_base is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver: WebDriver = driver_base
        if self.url != "":
            self.driver.get(self.url)

        # 隐式等待
        self.driver.implicitly_wait(5)
