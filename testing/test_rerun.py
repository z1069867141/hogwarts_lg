import pytest


def test_a():
    print("aaa")


@pytest.mark.flaky(reruns=5)
def test_b():
    assert False


def test_assume():
    pytest.assume(1 == 2)
    pytest.assume(2 == 3)
    pytest.assume(3 == 4)
    pytest.assume(4 == 4)
    pytest.assume(4 == 5)
