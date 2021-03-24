from appium import webdriver

from test_appium.data_driven.page.base_page import BasePage
from test_appium.data_driven.page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = '.view.WelcomeActivityAlias'
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "QV710BQF5F"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermissions"] = True
            caps['noReset'] = "true"  # 不清空缓存可以直接打开app
            caps['dontStopAppOnReset'] = 'true'  # 不停止app运行
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package, _activity)

        return self

    def main(self):
        return Main(self._driver)
