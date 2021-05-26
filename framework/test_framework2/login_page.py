from framework.test_framework2.base_page import BasePage


class LoginPage(BasePage):

    """
    当调用LoginPage的方法的时候调用不到
    借助于__getattr__方法实现任意方法的代理
    login.xxxxx =>login.__getattr__
    """
    def __getattr__(self, item):
        print(item)
        self._method = None
        # 当方法找不到的时候，调用一个通用方法进行处理
        return self._po_method

    # 定义通用方法
    def _po_method(self, *args, **kwargs):
        self.po_run(self._method, **kwargs)
    # def login_by_password(self, username, password):
    #     self.po_run("login_by_password", username=username, password=password)
