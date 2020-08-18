from typing import List


# 修改编码
import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 修改编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope='session')
def connDB():
    print("连接数据库")
    yield
    print("断开数据库")