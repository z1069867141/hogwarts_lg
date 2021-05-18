import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestDemo1:
    def setup_method(self, method):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo1(self):
        self.driver.get("https://ms.portal.azure.com/?AppPlatformExtension=canary#@microsoft.onmicrosoft.com/resource/subscriptions/6c933f90-8115-4392-90f2-7077c9fa5dbd/resourceGroups/vminh-v3-eastus/providers/Microsoft.AppPlatform/Spring/dvminh/troubleshooting")
        # self.driver.set_window_size(1536, 960)
        # self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        # # 断言
        # myclass = self.driver.find_element(By.LINK_TEXT, "所有分类").get_attribute("class")
        # assert "active" == myclass
        # time.sleep(5)
        # self.driver.find_element_by_css_selector("[placeholder='Search for common problems, tools and more']")
        frame = self.driver.find_element_by_xpath("//*[@class='fxs-part-frame']")
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@class='fxs-part-frame']"))
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@class='fxs-part-frame']"))
        self.driver.switch_to.frame("_react_frame_1")
        # self.driver.find_element_by_xpath("//*[@class='fxs-part-frame']").click()
        # self.driver.find_element_by_tag_name("input").click()
        # self.driver.find_element_by_class_name("form-control").click()
        print(text)
        # print(self.driver.find_element_by_id("page-description").text)
        # self.driver.find_element_by_class_name("search-input-group")

    def test_demo2(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=tryhtml_iframe_marginheight")
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='iframeResult']"))
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@src='demo_iframe.htm']"))
        # self.driver.find_element_by_xpath("//*[@class='fxs-part-frame']").click()
        # text = self.driver.find_element_by_xpath("//*[@class='app-nav-tab active']").text
        # print(self.driver.find_element_by_xpath("//*[@style='background-color:#F5DEB3']").text)
        self.driver.find_element_by_xpath("//*[@type='button']")
        # print(text)
        # print(self.driver.find_element_by_id("page-description").text)
        # self.driver.find_element_by_class_name("search-input-group")