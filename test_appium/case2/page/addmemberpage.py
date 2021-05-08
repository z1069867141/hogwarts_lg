from appium.webdriver.common.mobileby import MobileBy

from test_appium.case2.base.base_function import Base


class AddMemberPage(Base):
    addmember_element = (MobileBy.XPATH, "//*[@text='添加成员']")
    addmember_manual_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    toast_element = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')

    def goto_addmember_manual(self):
        from test_appium.case2.page.addmembermanualpage import AddMemberManualPage
        self.find_click(self.addmember_element)
        self.find_click(self.addmember_manual_element)
        return AddMemberManualPage(self.driver)

    def toast_text(self):
        text = self.get_text(self.toast_element)
        return text
