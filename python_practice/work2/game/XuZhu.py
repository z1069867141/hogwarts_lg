from python_practice.work2.game.TongLao import TongLao


class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")


a = XuZhu(100,100)
a.fight_zms(100,0.01)