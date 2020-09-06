from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage


class SettingMember(BasePage):
    delete_member_element = MobileBy.XPATH, "//*[@text='删除成员']"
    confirm_element = MobileBy.XPATH, "//*[@text='确定']"
    def delete_member(self):
        self.find_and_click(self.delete_member_element)
        self.find_and_click(self.confirm_element)
        from test_selenium.test_appium.page.addresslistpage import AddressListPage
        return AddressListPage(self.driver)