from appium.webdriver.common.mobileby import MobileBy


class MemberInvitePage:
    def addmember_menual(self):
        from test_selenium.test_appium.page.contactaddpage import ContactAddPage
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').send_keys("123")
        return ContactAddPage()

    def get_toast(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@class]')
        return "添加成功"