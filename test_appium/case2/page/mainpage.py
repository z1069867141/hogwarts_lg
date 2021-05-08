from appium.webdriver.common.mobileby import MobileBy

from test_appium.case2.base.base_function import Base
from test_appium.case2.page.addmemberpage import AddMemberPage


class MainPage(Base):
    contact_list_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def seleperson(self, name):
        return MobileBy.XPATH, f"//*[@text={name}]"

    def goto_addressbook(self):
        self.find_click(self.contact_list_element)
        return AddMemberPage(self.driver)

    def goto_SelectPerson(self, name):
        self.find_click(self.contact_list_element)
        self.find_click(self.seleperson(name))
        from test_appium.case2.page.persondetailpage import PersonDetailPage
        return PersonDetailPage(self.driver)

    def search_name(self, name):
        try:
            return self.get_text(self.seleperson(name))
        except:
            return "查找失败"
