from appium.webdriver.common.mobileby import MobileBy

from test_appium.case2.base.base_function import Base
from test_appium.case2.page.detailnextpage import DetailNextPage


class PersonDetailPage(Base):
    nextpage_element = (MobileBy.ID, "com.tencent.wework:id/h8g")

    def goto_detailnextpage(self):
        self.find_click(self.nextpage_element)
        return DetailNextPage(self.driver)