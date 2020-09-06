from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage


class MemberInvitePage(BasePage):
    addmember_menual_element = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
    def addmember_menual(self):
        from test_selenium.test_appium.page.contactaddpage import ContactAddPage
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find_and_click(self.addmember_menual_element)
        return ContactAddPage(self.driver)

    def get_toast(self):
        # toasttext = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        toasttext = self.get_toasttext()
        return toasttext