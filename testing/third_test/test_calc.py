import pytest
import yaml
import os

from pythoncode.calculator import Calculator


# 读取测试文件
def get_datas_add():
    mydatapath = os.path.dirname(__file__)+"./dates/calc.yml"
    with open(mydatapath, encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


# def get_datas_dive():
#     with open('./dates/calc.yml', encoding='utf-8') as f:
#         mydatas = yaml.safe_load(f)
#         adddatas = mydatas['dive']['datas']
#         myids = mydatas['dive']['myids']
#     return [adddatas, myids]


class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect', get_datas_add()[0], ids=get_datas_add()[1])
    def test_add(self, a, b, expect):
        """
        测试相加
        """
        result = self.calc.add(a, b)
        assert expect == result, f"计算错误，{expect}不等于{result}"

    # @pytest.mark.parametrize('a,b,expect', get_datas_dive()[0], ids=get_datas_dive()[1])
    # def test_sub(self, a, b, expect):
    #     """
    #     测试相减
    #     """
    #     try:
    #         result = self.calc.dive(a, b)
    #         assert expect == result, f"计算错误，{expect}不等于{result}"
    #     except:
    #         result_error = "错误"
    #         assert expect == result_error, f"计算错误，{expect}不等于{result}"
