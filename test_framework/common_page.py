from test_framework.base_page import BasePage
from test_framework.log import log


class CommonPage(BasePage):
    def __getattr__(self, item):
        """
        借助于__getattr__方法实现任意方法代理
        login.xxxx => login.__getattr__
        login.login_by_password => print
        print("156012345565","111111")

        下方代码代表，当你需要调用方法的时候，
        我直接给你调用_po_method这个方法
        """
        # log.debug(f'__get__attr__ {item}')
        self.method_name = item
        # 当方法找不到的时候我直接给你调用一个通用方法
        print(item)
        return self._po_method

    # 定义通用方法
    # 其中self.method_name是按照__getattr__中没有调用的方法作为了yaml中的search使用
    def _po_method(self, **kwargs):
        # log.debug(f"_po_method {kwargs}")
        self.po_run(self.method_name, **kwargs)

    # def login_by_password(self, username, password):
    #     self.po_run("login_by_password", username=username, password=password)
