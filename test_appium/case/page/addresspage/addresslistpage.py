from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.case.page.addresspage.memberinvitepage import MemberInvitePage
from test_appium.case.page.basepage import BasePage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmenmber_text = "添加成员"
    def add_member(self):
        """
        添加成员
        """
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().scrollable('
        #                          'true).instance(0)).scrollIntoView(new UiSelector('
        #                          ').text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self.addmenmber_text)
        return MemberInvitePage(self.driver)
