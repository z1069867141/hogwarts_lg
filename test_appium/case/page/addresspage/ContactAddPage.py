# from test_appium.cases.page.addresspage.memberinvitepage import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.case.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    name_element = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText')
    gender_element = (MobileBy.XPATH, '//*[@text="男"]')
    male_element = (MobileBy.XPATH, '//*[@text="男"]')
    female_element = (MobileBy.XPATH, '//*[@text="女"]')
    phonenum_element = (MobileBy.ID, "com.tencent.wework:id/f4m")
    save_element = (MobileBy.XPATH, '//*[@text="保存"]')

    def edit_name(self, name):
        self.find_and_sendkeys(self.name_element, name)
        return self

    def edit_gender(self, gender):
        self.find_and_click(self.gender_element)
        if gender == "男":
            self.find_and_click(self.male_element)
        else:
            self.find_and_click(self.female_element)
        return self

    def edit_phonenum(self, phonenum):
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self

    def click_save(self):
        self.find_and_click(self.save_element)
        from test_appium.case.page.addresspage.memberinvitepage import MemberInvitePage
        return MemberInvitePage(self.driver)
