import pytest

from test_framework.base_page import BasePage
from test_framework.demo_page import DemoPage
from test_framework.login_page import LoginPage
from test_framework.utils import Utils


class TestLogin:
    testcase_file = 'test_search.yaml'
    po_file = 'page_demo.yaml'
    data = Utils.from_file(testcase_file)

    def setup_class(self):
        self.app = BasePage()
        self.app.start()

        self.demo = DemoPage(self.po_file)

    def setup(self):
        pass

    # def teardown(self):
    #     self.demo.back()

    def teardown_class(self):
        self.app.stop()

    # todo: 测试数据的数据驱动
    # @pytest.mark.parametrize("username, password", [
    #     ("user1", "password1"),
    #     ("user2", "password2")
    # ])
    def test_login(self):
        po_file = "page_login.yaml"
        login = LoginPage(po_file)
        login.login_by_password('18018845546', '111111')

    # @pytest.mark.parametrize("keyword", [
    #     'alibaba',
    #     'baidu',
    #     'jd'
    # ])

    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        self.demo.search(keyword)
        self.demo.back()