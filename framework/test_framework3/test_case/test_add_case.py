import pytest

from framework.test_framework3.page.address_book_main_page import MainPage


class TestAdd:
    def teardown_method(self):
        self.main.driver.quit()

    def test_add_department(self):
        # 1.进入通讯录页 2.添加部门
        self.main = MainPage("https://work.weixin.qq.com/wework_admin/frame#contacts")
        assert "新建部门成功" == self.main.go_to_add_apartment().add_apartment()
