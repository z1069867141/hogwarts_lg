import pytest

from test_framework.base_page import BasePage
from test_framework.demo_page import DemoPage
from test_framework.common_page import CommonPage
from test_framework.utils import Utils


class TestLogin:
    testcase_file = 'test_search.yaml'
    po_file = 'page_demo.yaml'
    data = Utils.from_file(testcase_file)

    def setup_class(self):
        """
        由于在使用Demopage的时候,调用start并不会将类里的_driver调用会让_driver一直处于None,
        需要先调用app.start()让类里的_driver有值才行，不然会提示_driver使用find_element搜索element是空的
        :return:
        """
        self.app = BasePage()
        self.app.start()

        # self.demo = DemoPage(self.po_file)
        # self.demo.start()

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
        login = CommonPage(po_file)
        login.login_by_password(username='18018845546', password='111111')

    # @pytest.mark.parametrize("keyword", [
    #     'alibaba',
    #     'baidu',
    #     'jd'
    # ])

    # @pytest.mark.parametrize(data['keys'], data['values'])
    # def test_search(self, keyword):
    #     self.demo = DemoPage(self.po_file)
    #     self.demo.search(keyword)
    #     self.demo.back()

    # 用common page来代替
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search_common(self, keyword):
        demo = CommonPage(self.po_file)
        demo.search(keyword=keyword)
        demo.back()