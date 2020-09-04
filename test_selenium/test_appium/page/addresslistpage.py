from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage
from test_selenium.test_appium.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    def add_member(self):
        """
        添加成员
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                               'true).instance(0)).scrollIntoView(new UiSelector('
                                                               ').text("添加成员").instance(0));').click()
        return MemberInvitePage(self.driver)
