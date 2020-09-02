from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppium:
    def setup(self):
        var = {
            "deviceName": "7c63d4cd",
            "platformName": "android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", var)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 删除联系人步骤，通过搜索删除的用户，断言用户是否存在
    def test_deleteContact(self):
        name = "测试人2"

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='测试人']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b53").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys(name)
        searchResult = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c5m").text
        assert "无搜索结果" == searchResult
