from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.case.page.addresspage.addresslistpage import AddressListPage
from test_appium.case.page.basepage import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_addresslist(self):
        self.find_and_click(self.addresslist_element)
        return AddressListPage(self.driver)
