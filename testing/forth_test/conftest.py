import pytest
import yaml

from testing.forth_test.calculator import Calculator


@pytest.fixture(scope="module")
def get_cal():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")


def get_data_add():
    with open("./dates/calc.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        adddata = data["add"]['datas']
        addids = data["add"]["myids"]
        return [adddata, addids]


@pytest.fixture(params=get_data_add()[0],ids=get_data_add()[1],scope='function')
def get_datas_add(request):
    return request.param


def get_data_sub():
    with open("./dates/calc.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        adddata = data["sub"]['datas']
        addids = data["sub"]["myids"]
        return [adddata, addids]


@pytest.fixture(params=get_data_sub()[0],ids=get_data_sub()[1],scope='function')
def get_datas_sub(request):
    return request.param


def get_data_dive():
    with open("./dates/calc.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        adddata = data["dive"]['datas']
        addids = data["dive"]["myids"]
        return [adddata, addids]


@pytest.fixture(params=get_data_dive()[0],ids=get_data_dive()[1],scope='function')
def get_datas_dive(request):
    return request.param


def get_data_mun():
    with open("./dates/calc.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        adddata = data["mun"]['datas']
        addids = data["mun"]["myids"]
        return [adddata, addids]


@pytest.fixture(params=get_data_mun()[0],ids=get_data_mun()[1],scope='function')
def get_datas_mun(request):
    return request.param