from appium import webdriver


class TestAppium:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0'
        desired_caps['deviceName'] = 'QV710BQF5F'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = "true"  # 不清空缓存可以直接打开app
        desired_caps['dontStopAppOnReset'] = 'true'  # 不停止app运行
        desired_caps['skipDeviceInitialization'] = "true"
        # 让app能够输入中文
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['presetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()