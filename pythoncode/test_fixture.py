import pytest


@pytest.fixture(autouse=True)
def login():
    print("登录")
    username = "Tom"
    password = 123456
    yield [username, password]
    print("登出")


def test_case1():
    print(f"测试用例1-需要登陆{login}")


def test_case2():
    print("测试用例2")


def test_case3():
    print(f"测试用例3-需要登陆{login}")


def test_case4():
    print("case4")
    print(login)
