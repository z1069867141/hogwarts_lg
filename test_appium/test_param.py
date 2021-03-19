import pytest
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *

from test_appium.test_appium import TestAppium


class Testcase(TestAppium):
    @pytest.mark.parametrize('searchkey, type, expect_price', [
        ('alibaba', 'BABA', 230),
        ('xiaomi', '01810', 26)
    ])
    def test_search(self, searchkey, type, expect_price):
        """
        1.打开 雪球应用
        2.点击 搜索框
        3.输入 搜索词‘alibaba’或‘xiaomi’...
        4.点击第一个搜索结果
        5.判断 股票价格
        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        current_price_element = self.driver.find_element(MobileBy.XPATH,
                                                         f"//*[@text='{type}']/../../..//*["
                                                         "@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(current_price_element.text)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
