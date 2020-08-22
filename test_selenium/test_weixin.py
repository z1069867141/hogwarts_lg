import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo1:
    def setup_method(self, method):
        option = Options()
        # option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo1(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.set_window_size(1536, 960)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        # 断言
        myclass = self.driver.find_element(By.LINK_TEXT, "所有分类").get_attribute("class")
        assert "active" == myclass

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853785096086'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '2F5URkk21A8wFu8MT7ujN5pXw2CKr96O5N8VANNoLSkk3JcIAkWk26LI3v-DS0Y6qG_NCZgUflSQNhO3piLxL3r15ptkz0A5lTiwFc1p9ia4HgG45BMMWPFpZ1NI9_XMK0jh-ATk9VD6FdYZqYo6Qsho42j2UdG2KU16xABdN4ML11o39S7VCLDxP3S2M-qQMidisDcqh7tPtzIiR7m6OUayypAc8AuDPvNHXPVniYCN1lorpMSdsR63BG9zh7Eg4CpLoVhO2tI16b0O301IbQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853785096086'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324963157999'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Eod4rdiCNOPsXynJl0bFTebDzNllBEp6ZEYRSVx3uRMq5pvEPt_CA6gVe1puhF1T'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9596977'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598158584, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1vv73jg'}, {'domain': '.qq.com', 'expiry': 1598213559, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1357498016.1598127049'}, {'domain': '.qq.com', 'expiry': 1661199159, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1465356624.1598127049'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629663048, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '8eb59ae156c599fb639ca554754187eebbf45f5206611db9b5329dcfc7a8833a'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '3043088800'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '9Z6hrLnWf4'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600719161, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-tw%2Ccht'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2957135973750677'}, {'domain': '.qq.com', 'expiry': 1598127211, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2256359424'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(10)

    def test_cookie1(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853785096086'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '2F5URkk21A8wFu8MT7ujN5pXw2CKr96O5N8VANNoLSkk3JcIAkWk26LI3v-DS0Y6qG_NCZgUflSQNhO3piLxL3r15ptkz0A5lTiwFc1p9ia4HgG45BMMWPFpZ1NI9_XMK0jh-ATk9VD6FdYZqYo6Qsho42j2UdG2KU16xABdN4ML11o39S7VCLDxP3S2M-qQMidisDcqh7tPtzIiR7m6OUayypAc8AuDPvNHXPVniYCN1lorpMSdsR63BG9zh7Eg4CpLoVhO2tI16b0O301IbQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853785096086'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324963157999'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'Eod4rdiCNOPsXynJl0bFTebDzNllBEp6ZEYRSVx3uRMq5pvEPt_CA6gVe1puhF1T'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9596977'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598158584, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1vv73jg'},
            {'domain': '.qq.com', 'expiry': 1598213559, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1357498016.1598127049'},
            {'domain': '.qq.com', 'expiry': 1661199159, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1465356624.1598127049'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629663048, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '8eb59ae156c599fb639ca554754187eebbf45f5206611db9b5329dcfc7a8833a'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '3043088800'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': '9Z6hrLnWf4'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600719161, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-tw%2Ccht'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '2957135973750677'},
            {'domain': '.qq.com', 'expiry': 1598127211, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '2256359424'}]
        db = shelve.open("mydb/logincookies")
        db['cookie'] = cookies
        db.close()