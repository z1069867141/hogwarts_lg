import pytest

from framework.test_framework2.base_page import BasePage
from framework.test_framework2.demo_page import DemoPage
from framework.test_framework2.common_page import CommonPage
from framework.test_framework2.utils import Utils


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
    # self.demo.back()

    def teardown_class(self):
        self.demo.stop()

    # todo: 测试数据的数据驱动
    @pytest.mark.parametrize("username, password", [
        ("user1", "password1"),
        ("user2", "password2")
    ])
    def test_login(self, username, password):
        # todo: 测试步骤的数据驱动
        self.demo.login(username, password)
        assert 1 == 1

    # @pytest.mark.parametrize("keyword", [
    #     'alibaba',
    #     # 'baidu',
    #     # 'jd'
    # ])
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        self.demo.search(keyword)

    # 用common page代替
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search_common_page(self, keyword):
        # todo:python元编程实现python的数据驱动
        demo = CommonPage(self.po_file)
        demo.search(keyword=keyword)
        demo.back()

    def test_login(self):
        po_file = 'page_login.yaml'
        login = CommonPage(po_file)
        login.login_by_password('151098231234', '2314987')
