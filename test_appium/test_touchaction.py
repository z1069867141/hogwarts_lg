from appium.webdriver.common.touch_action import TouchAction

from test_appium.test_appium import TestAppium


class TestCase:
    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        action.press()  # press中可以输入元素参数用于定位，不止限于坐标
