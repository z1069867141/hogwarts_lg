from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage


class SearchContactMember(BasePage):
    search_member_page_element = (MobileBy.ID, "com.tencent.wework:id/g75")
    def search_member(self, member):
        self.find_and_sendkeys(self.search_member_page_element, member)
        return self

    result_element = (MobileBy.ID, "com.tencent.wework:id/c5m")
    def result_member(self):
        # try:
        #     text = self.get_text(self.result_element)
        #     return text
        # except:
        #     return "存在该元素"
        text = self.get_text(self.result_element)
        return text