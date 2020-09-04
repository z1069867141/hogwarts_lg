from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage


class MemberInvitePage(BasePage):
    def addmember_menual(self):
        from test_selenium.test_appium.page.contactaddpage import ContactAddPage
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAddPage(self.driver)

    def get_toast(self):
        toasttext = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return toasttext