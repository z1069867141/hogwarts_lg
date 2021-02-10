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