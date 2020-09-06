from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage


class ContactAddPage(BasePage):
    name_element = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText')
    gender_element = (MobileBy.XPATH, '//*[@text="男"]')
    male_element = (MobileBy.XPATH, '//*[@text="男"]')
    female_element = (MobileBy.XPATH, '//*[@text="女"]')
    phonenum_element = (MobileBy.ID, "com.tencent.wework:id/f9s")
    save_element = (MobileBy.XPATH, '//*[@text="保存"]')
    def edit_name(self, name):
        self.find_and_sendkeys(self.name_element,name)
        return self

    def edit_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        # if gender == "男":
        #     self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        # return self
        self.find_and_click(self.gender_element)
        if gender == "男":
            self.find_and_click(self.male_element)
        else:
            self.find_and_click(self.female_element)
        return self

    def edit_phonenum(self, phonenum):
        self.find_and_sendkeys(self.phonenum_element,phonenum)
        return self

    def click_save(self):
        self.find_and_click(self.save_element)
        from test_selenium.test_appium.page.memberinvitepage import MemberInvitePage #通过使用局部导入只有在用这个方法的时候才调用，防止全局导入的时候初始化代码报错提示导入循环造成问题
        return MemberInvitePage(self.driver)

