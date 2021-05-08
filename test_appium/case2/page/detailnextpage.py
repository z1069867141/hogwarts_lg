from appium.webdriver.common.mobileby import MobileBy

from test_appium.case2.base.base_function import Base
from test_appium.case2.page.editmemberpage import EditMemberPage


class DetailNextPage(Base):
    nextpage_element = (MobileBy.ID, "com.tencent.wework:id/b49")

    def goto_editpage(self):
        self.find_click(self.nextpage_element)
        return EditMemberPage(self.driver)