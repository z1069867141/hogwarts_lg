"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""


def game():
    my_hp = 1000
    my_power = 200
    enemy_hp = 999
    enemy_power = 199
    while True:
        my_hp = my_hp - enemy_power     # 通过循环我的血量每次扣减后，当前的血量值
        enemy_hp = enemy_hp - my_power  # 通过循环敌人的血量每次扣减后，当前的血量值
        print(my_hp)                    # 打印我的血量
        if my_hp <= 0:                  # 我的血量小于等于0就是我输了，然后跳出循环
            print("我输了")
            break
        elif enemy_hp <= 0:             # 滴人血量小于等于0就是我输了，然后跳出循环
            print("你输了")
            break


game()