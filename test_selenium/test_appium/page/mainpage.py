from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.addresslistpage import AddressListPage


class MainPage:
    def gtoto_addresslist(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage()