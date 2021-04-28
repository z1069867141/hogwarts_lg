from appium.webdriver.common.mobileby import MobileBy

class mainpage():
    def __init__(self, driver):
        self.driver = driver

    def click_contact_list(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()