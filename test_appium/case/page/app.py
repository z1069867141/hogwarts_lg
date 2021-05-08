from appium import webdriver

from test_appium.case.page.basepage import BasePage
from test_appium.case.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        """
        启动应用
        如果driver已经被实例化，就复用已有的driver
        如果driver=None,就要重新创建一个driver
        """
        if self.driver == None:
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
        else:
            # 启动caps里面设置的appPAckage appActivity
            self.driver.launch_app()  # 也可以使用start_activity()但是需要传入包名和activity
        return self  # 只是为了返回到自身

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
