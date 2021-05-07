import pytest
import yaml

from test_appium.case.page.app import App


def get_contact():
    with open("../datas/contacts.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


class Testcase:
    def setup(self):
        """
        启动应用
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum', get_contact())
    def test_addcontact(self, name, gender, phonenum):
        mypage = self.main.goto_addresslist().add_member().addmember_manual() \
            .edit_name(name).edit_phonenum(phonenum) \
            .click_save()
        mytoast = mypage.get_toast()
        assert mytoast == "添加成功"
