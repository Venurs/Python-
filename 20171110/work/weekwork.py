"""
掷筛子
"""


import random
play_money = 5000
print("===============欢迎来到不坑你坑谁赌场===================")
while True:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    result = num1 + num2 + num3
    choose = input("玩家请押大小：")
    put_money = int(input("玩家请下注："))
    while True:
        if put_money % 50 == 0 and put_money != 0 and put_money <= 1000:
            if play_money >= put_money:
                print("下注成功")
                if (result >= 11 and choose == "大") or (result <= 10 and choose == "小"):
                    play_money += put_money
                    print("恭喜您赢得%d,当前账户余额%d" % (put_money, play_money))
                else:
                    play_money -= put_money
                    print("很遗憾您输掉%d,当前账户余额%d" % (put_money, play_money))
                break
            else:
                print("您账户余额为%d,无法继续游戏,您可在一下三项中选择一项：" % play_money)
                print("A：充值")
                print("B:重新下注")
                print("C:退出")
                print("")
                no_money_choose = input("请输入A,B,C进行选择：")
                if no_money_choose == "A":
                    print("正在加载支付宝页面，请稍等。。。")
                    add_money = int(input("充值后将直接下注，请输入充值金额："))
                    play_money += add_money
                    print("充值成功，您当前账户余额%d" % play_money)
                elif no_money_choose == "B":
                    put_money = int(input("玩家请重新下注："))
                elif no_money_choose == "C":
                    print("您已退出游戏，欢迎下次光临")
                    break
        elif put_money > 1000:
            put_money = int(input("下注金额不能大于1000，玩家请重新下注："))
        elif put_money == 0:
            put_money = int(input("下注金额不能为0，玩家请重新下注："))
        else:
            put_money = int(input("下注金额为50的倍数，玩家请重新下注："))

