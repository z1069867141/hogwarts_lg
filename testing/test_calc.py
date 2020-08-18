import pytest
import yaml
import os
import sys
from hogwarts_lg.pythoncode.calculator import Calculator

'''
pytest 命名规则
文件名：以test_开头 （test_*.py)
类名：以test 开头
方法名： 以test_开头
'''


# 读取测试文件
def get_datas():
    with open('./dates/calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def get_datas(request):
    return request.param


class TestCalc:

    def test_add(self, get_calc, get_datas):
        """
        测试相加
        """
        # calc = Calculator()
        result = get_calc.add(get_datas[0], get_datas[1])
        assert get_datas[2] == result

    # @pytest.mark.parametrize('a,b,expect', [
    #     (0.1, 0.2, 0.3)
    # ], ids=['float'])
    # def test_add(self, a, b, expect):
    #     """
    #     测试相加
    #     """
    #     # calc = Calculator()
    #     result = self.calc.add(a, b)
    #     assert expect == result
