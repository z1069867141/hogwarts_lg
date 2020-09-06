from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage
from test_selenium.test_appium.page.settingmemberpage import SettingMember


class ContactDetailpage(BasePage):
    setting_member = (MobileBy.ID, "com.tencent.wework:id/hjz")
    setting_edit_member = (MobileBy.ID, "com.tencent.wework:id/b53")
    def click_setting_member(self):
        """
        进入编辑成员页面
        :return:
        """
        self.find_and_click(self.setting_member)  # 进入个人信息设置界面
        self.find_and_click(self.setting_edit_member)  # 进入编辑成员界面
        return SettingMember(self.driver)
