from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.memberinvitepage import MemberInvitePage


class AddressListPage:
    def add_member(self):
        """
        添加成员
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new Uiselector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new Uiselector()'
                                 '.text("添加成员").instance(0));').clcik()
        return MemberInvitePage()
