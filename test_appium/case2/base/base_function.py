from appium.webdriver.webdriver import WebDriver


class Base:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator):
        return self._driver.find_element(*locator)

    def find_click(self, locator):
        self.find(locator).click()

    def find_sendkeys(self, locator, value):
        self.find(locator).send_keys(value)

    def get_text(self, locator):
        text = self.find(locator).text
        return text