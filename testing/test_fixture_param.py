import pytest


@pytest.fixture(params=[('tom', 123456), ('jerry', 654321)], ids=['用户Tom', '用户jerry'])
def login(request):
    return request.param


def test_case(login):
    print(f"username:{login[0]},password:{login[1]}")
    print("cases")