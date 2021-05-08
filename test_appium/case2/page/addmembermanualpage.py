from appium.webdriver.common.mobileby import MobileBy

from test_appium.case2.base.base_function import Base


class AddMemberManualPage(Base):
    name_element = (MobileBy.ID, "com.tencent.wework:id/ays")
    phonenum_element = (MobileBy.ID, "com.tencent.wework:id/f4m")
    save_element = (MobileBy.ID, "com.tencent.wework:id/ac9")
    def edit_name(self, name):
        self.find_sendkeys(self.name_element, name)
        return self

    def edit_phonenum(self, phonenum):
        self.find_sendkeys(self.phonenum_element, phonenum)
        return self

    def click_save(self):
        self.find_click(self.save_element)
        from test_appium.case2.page.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)
