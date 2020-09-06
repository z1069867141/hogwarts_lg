from appium.webdriver.common.mobileby import MobileBy

from test_selenium.test_appium.page.basepage import BasePage
from test_selenium.test_appium.page.contactdetailpage import ContactDetailpage
from test_selenium.test_appium.page.memberinvitepage import MemberInvitePage
from test_selenium.test_appium.page.searchcontactmemberpage import SearchContactMember


class AddressListPage(BasePage):
    addmember_text = "添加成员"
    def add_member(self):
        """
        添加成员
        """
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
        #                                                        'true).instance(0)).scrollIntoView(new UiSelector('
        #                                                        ').text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self.addmember_text)
        return MemberInvitePage(self.driver)

    def click_contact_detail(self, member_name):
        """
        选择成员进入个人信息页
        :return:self
        """
        member_name = MobileBy.XPATH, f"//*[@text='{member_name}']"
        self.find_and_click(member_name)
        return ContactDetailpage(self.driver)

    search_element = MobileBy.ID, "com.tencent.wework:id/hk9"
    def click_search_page(self):
        self.find_and_click(self.search_element)
        return SearchContactMember(self.driver)
