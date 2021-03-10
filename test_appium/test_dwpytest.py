from test_appium.test_appium import TestAppium

class TestCase(TestAppium):
    def test_attr(self):
        """
        打开【雪球】应用首页
        定位首页的搜索框
        判断搜索框的是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        像搜索框输入:alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        search_enabled = element.is_enabled()
        #打印元素中的文本
        print(element.text)
        #打印元素的位置
        print(element.location)
        #打印元素的尺寸
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # 选中元素返回的是string类型的ture和false
            element_display = alibaba_element.get_attribute("displayed")
            # 下方使用if的使用需要使用string类型的字符
            if element_display == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_get_current(self):
        """
        打开【雪球】应用搜索阿里巴巴-sw，之后答应股票目前的价格
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        prise = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(prise)
        assert float(prise) > 100

    def test_myinfo(self):
        """
        1.点击我的，进入到个人信息页面
        2.点击登录，进入登陆页面
        3.输入用户名，输入密码
        4.点击登录
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("1234")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId(com.xueqiu.android:id/tab_name).text("我的")。className("")')