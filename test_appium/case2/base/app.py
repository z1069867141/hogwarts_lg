from appium import webdriver

from test_appium.case2.base.base_function import Base
from test_appium.case2.page.mainpage import MainPage


class App:
    def start(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '11.0'
        # desired_caps['deviceName'] = 'QV710BQF5F'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = "true"  # 不清空缓存可以直接打开app
        # desired_caps['dontStopAppOnReset'] = 'true'  # 不停止app运行
        # desired_caps['skipDeviceInitialization'] = "true"
        # 让app能够输入中文
        # desired_caps['unicodeKeyBoard'] = 'true'
        # desired_caps['presetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
