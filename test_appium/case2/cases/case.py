import pytest
import yaml

from test_appium.case2.base.app import App


def get_contact():
    with open("../config/contacts.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


class Testcase:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name, phonenum", get_contact())
    def test_AddContactPerson(self, name, phonenum):
        result = self.main.goto_addressbook() \
            .goto_addmember_manual().edit_name(name). \
            edit_phonenum(phonenum).click_save().toast_text()
        assert result == "添加成功"

    @pytest.mark.parametrize("name, phonenum", get_contact())
    def test_deletePerson(self, name, phonenum):
        result = self.main.goto_SelectPerson(name).\
            goto_detailnextpage().goto_editpage().\
            delete().delete_confirm().search_name(name)
        assert result == "查找失败"
