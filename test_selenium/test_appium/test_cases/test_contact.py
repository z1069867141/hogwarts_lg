import pytest
import yaml

from test_selenium.test_appium.page.app import App


def get_contact():
    with open("../datas/contacts.yaml") as f:
        datas = yaml.safe_load(f)
        return datas


class TestWeixin:
    def setup(self):
        """
        启动app
        通过self.app.start().goto_main()调用启动页面之后在主动进入主界面
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        """
        关闭app
        """
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum', get_contact())
    def test_addcontact(self, name, gender, phonenum):
        """
        通过使用\来代码换行
        进入手动添加成员页面
        """
        my_page = self.main.gtoto_addresslist().add_member().addmember_menual() \
            .edit_name(name).edit_gender(gender).edit_phonenum(phonenum) \
            .click_save()

        my_toast = my_page.get_toast()
        assert my_toast == "添加成功"
