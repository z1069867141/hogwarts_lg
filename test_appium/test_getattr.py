from test_appium.test_appium import TestAppium
from hamcrest import *


class Testgetattribute(TestAppium):
    def test_get_attr(self):
        # search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        # print(search_ele.get_attribute("clickable"))
        assert_that(10, equal_to(9), "这是一个提示")
