import time

from appium.webdriver.extensions.android.gsm import GsmCallActions

from test_appium.test_appium import TestAppium
from hamcrest import *


class Testgetattribute(TestAppium):
    def test_get_attr(self):
        # search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        # print(search_ele.get_attribute("clickable"))
        assert_that(10, equal_to(9), "这是一个提示")

    def test_mobile(self):
        # self.driver.make_gsm_call('15012345678', GsmCallActions.CALL)
        # self.driver.send_sms('15012345678', 'hello appium api')
        # self.driver.set_network_connection(1)
        # time.sleep(5)
        # self.driver.set_network_connection(2)
        self.driver.start_recording_screen()
        self.driver.get_screenshot_as_file('img.png')
        time.sleep(5)
        self.driver.stop_recording_screen()