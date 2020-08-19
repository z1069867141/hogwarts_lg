import pytest

class Testcalc:
    def test_add(self, get_cal, get_datas_add):
        result = get_cal.add(get_datas_add[0],get_datas_add[1])
        assert result == get_datas_add[2]

    def test_sub(self, get_cal, get_datas_sub):
        result = get_cal.sub(get_datas_sub[0],get_datas_sub[1])
        assert result == get_datas_sub[2]

    def test_dive(self, get_cal, get_datas_dive):
        try:
            result = get_cal.dive(get_datas_dive[0],get_datas_dive[1])
        except:
            result = "错误"
        assert result == get_datas_dive[2]

    def test_mun(self, get_cal, get_datas_mun):
        result = get_cal.mun(get_datas_mun[0],get_datas_mun[1])
        assert result == get_datas_mun[2]