"""
App 类：
app 常用的方法：比如 启动应用，关闭应用，重启应用，进入首页
"""
from appium import webdriver

from test_selenium.test_appium.page.mainpage import MainPage


class App:
    """
    return:返回调用自己可以促使接下来继续调用自身类的其他方法
    """
    def start(self):
        caps = {}
        caps['platformName'] = "android"
        caps['deviceName'] = "hogwarts"
        caps['appPackage'] = "com.tencent.wework"
        caps['appActivity'] = ".launch.LaunchSplashActivity"
        caps['noRest'] = "True"

        self.driver = webdriver.Remote("https://localhost:4723/wd/hub", caps)

        self.driver.implicitly_wait(5)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self) -> MainPage:
        return MainPage()
