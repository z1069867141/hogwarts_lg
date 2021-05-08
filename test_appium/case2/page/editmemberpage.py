from appium.webdriver.common.mobileby import MobileBy

from test_appium.case2.base.base_function import Base


class EditMemberPage(Base):
    delete_element = (MobileBy.ID, "com.tencent.wework:id/e37")
    delete_confirm_element = (MobileBy.ID, "com.tencent.wework:id/bei")

    def delete(self):
        self.find_click(self.delete_element)
        return self

    def delete_confirm(self):
        self.find_click(self.delete_confirm_element)
        from test_appium.case2.page.mainpage import MainPage
        return MainPage(self.driver)