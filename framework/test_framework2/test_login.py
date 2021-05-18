import pytest

from framework.test_framework2.demo_page import demo


class TestLogin:
    def setup(self):
        self.demo = demo()

    @pytest.mark.parametrize("username, password", [
        ("user1", "password1"),
        ("user2", "password2")
    ])
    def test_login(self, username, password):
        self.demo.login(username, password)
        assert 1 == 1
