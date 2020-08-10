class TongLao(object):
    def __init__(self, Hp, Power):
        self.Hp = Hp
        self.Power = Power

    def see_people(self, name):
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self, Hp, Power):
        enemy_hp = Hp / 2
        enemy_power = Power * 10
        my_final_hp = self.Hp - enemy_power
        enemy_final_hp = enemy_hp - self.Power
        print("我方获胜") if my_final_hp > enemy_final_hp else print("敌方赢了")

#
# a = TongLao(100, 100)
# a.see_people("丁春秋")
# a.fight_zms(50, 0.01)
