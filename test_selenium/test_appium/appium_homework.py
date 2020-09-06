import pytest
import yaml

from test_selenium.test_appium.page.app import App


def get_contact():
    with open('./datas/contactsl.yaml') as f:
        datas = yaml.safe_load(f)
    return datas


class TestWeixin:
    def setup(self):
        """
        启动app
        通过self.app.start().goto_main()调用启动页面之后在主动进入主界面
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        """
        关闭app
        """
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum', get_contact())
    def test_addcontact(self, name, gender, phonenum):
        """
        通过使用\来代码换行
        进入手动添加成员页面
        """
        my_page = self.main.gtoto_addresslist().add_member().addmember_menual() \
            .edit_name(name).edit_gender(gender).edit_phonenum(phonenum) \
            .click_save()

        my_toast = my_page.get_toast()
        assert my_toast == "添加成功"

    @pytest.mark.parametrize('name, gender, phonenum', get_contact())
    def test_deletecontact(self, name, gender, phonenum):
        my_page = self.main.gtoto_addresslist().click_contact_detail(name).click_setting_member().delete_member() \
            .click_search_page()

        result = my_page.search_member(name).result_member()
        assert result == "无搜索结果"





# import pytest
# import yaml
# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
#
# def get_contact():
#     with open("./datas/contacts.yml") as f:
#         datas = yaml.safe_load(f)
#     return datas
#
# class TestAppium:
#     def setup(self):
#         var = {
#             "deviceName": "7c63d4cd",
#             "platformName": "android",
#             "appPackage": "com.tencent.wework",
#             "appActivity": ".launch.LaunchSplashActivity",
#             "noReset": "True"
#         }
#         self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", var)
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     @pytest.mark.parametrize("name,gender,phonenum",get_contact())
#     def test_addcontact(self,name,gender, phonenum):
#         pass

    # # 删除联系人步骤，通过搜索删除的用户，断言用户是否存在
    # def test_deleteContact(self):
    #     name = "测试人2"
    #
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='测试人']").click()
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b53").click()
    #     """
    #     1. UI Automator locator是调用了Android SDK的内容, 所有具体的类文档可以参考: https://developer.android.com/reference/android/support/test/uiautomator/UiSelector.html
    #     2. 使用UI Automator locator, 在UI Automator Viewer里见到的所有元素的属性都可以用来查找元素, 但对应的方法名不一定与UI Automator Viewer里是一样的,所以具体还是要参看上面的连接
    #     3. 常用的有:
    #     a. 通过index查找: driver.find_element_by_android_uiautomator("new UiSelector().index(5)")
    #     b. 通过text查找: driver.find_element_by_android_uiautomator("new UiSelector().text(\"6\")")
    #     c. 通过clickable查找: driver.find_element_by_android_uiautomator("new UiSelector().clickable(true)")
    #     d. 通过content-desc查找: driver.find_element_by_android_uiautomator("new UiSelector().description(\"\equals")")
    #     e. 通过resource-id查找: driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"com.android.calculator2:id/digit_3\")")
    #     f. 通过两个以上属性共同查找: driver.find_element_by_android_uiautomator("new UiSelector().clickable(true).index(5)")
    #     """
    #     self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,              #通过滑轮搜索元素，查找是否有符合的元素
    #                              'new UisScrollable(new Uiselector()'
    #                              '.scrollable(true),instance(0))'
    #                              '.scrollIntoView(new UiSelector()'
    #                              '.text("删除成员").instance(0));').click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys(name)
    #     searchResult = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c5m").text
    #     assert "无搜索结果" == searchResult
