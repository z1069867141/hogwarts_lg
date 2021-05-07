# from test_appium.case.page.addresspage.ContactAddPage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.case.page.basepage import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_manual_element = (MobileBy.XPATH, "//*//*[@text='手动输入添加']")
    get_toast_element = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')

    def addmember_manual(self):
        self.find_and_click(self.addmember_manual_element)
        from test_appium.case.page.addresspage.ContactAddPage import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        toasttext = self.get_text(self.get_toast_element)
        return toasttext
