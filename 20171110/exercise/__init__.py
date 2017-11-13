"""
打印2-100之间。求素数，也叫质数。(只能被1和本身整除的数)
100元钱，买100只鸡。公鸡5元一个，母鸡3元一个，小鸡1元3个。
break，continue结束 循环：while
两层while循环？。。
"""
import random
# i = 2
# while i <= 100:
#     j = 2
#     while j <= i - 1:
#         if i % j == 0:
#             break
#         else:
#             if j == i - 1:
#                 print(i, end=" ")
#                 break
#             j += 1
#             continue
#     i += 1


# i = 0  # 公鸡
# while i <= 20:
#     j = 0  # 母鸡
#     while j <= 34:
#         m = 0
#         while m <= 100 - i - j:
#             if ((i * 5) + (j * 3) + (100 - i - j) * 0.3) == 100:
#                 print(i, j, 100 - i - j)
#                 break
#             m += 1
#         j += 1
#     i += 1

# def put():
#     if system == 1:
#         print("系统出拳，剪刀")
#     elif system == 2:
#         print("系统出拳，石头")
#     elif system == 3:
#         print("系统出拳，布")
#
#
# print("1,剪刀。。2，石头。。3，布。。")
# while True:
#     system = random.randint(1, 3)
#     # print(system)
#     play = int(input("请玩家猜拳："))
#     if system == play:
#         print("平局", end=",")
#         put()
#     elif (system == 1 and play == 3) or (system == 2 and play == 1) or (system == 3 and play == 2):
#         print("系统赢", end=",")
#         put()
#     elif (system == 3 and play == 1) or (system == 1 and play == 2) or (system == 2 and play == 3):
#         print("玩家赢", end=",")
#         put()
#     elif play > 3 or play < 1:
#         print("输入无效,游戏结束")
#         break


import random

money = 5000
while True:
    num1 = random.randint(3, 18)
    # 大：11,12,13,14,15,16,17,18
    # 小：3,4,5,6,7,8,9,10
    # 玩家起始金额 5000
    begin = int(input("请输入 1 开始 2 退出"))
    if begin == 1:
        stake = int(input("请输入要下的赌注,必须是50的倍数，不得超过1000"))
        if stake % 50 == 0 and 50 <= stake <= 1000:
            i = input("请输入您的选择:大, 小")
            # 结果：大（num1 > 10) 小（num1 <= 10)
            if (i == "大" and num1 > 10) or (i == "小" and num1 <= 10):
                money += stake
                print("系统点数：%d, 您选择了：%s。恭喜您赢了，当前余额为:%d" % (num1, "i", money))
                if (i == "大" and num1 <= 10) or (i == "小" and num1 > 10):
                    money -= stake
                    print("系统点数: %d, 您选择了: %s。很遗憾您输了，当前余额为: %d" % (num1, "i", money))
        elif stake % 50 != 0 or stake > 1000:
            print("请输入正确的赌注金额")
        elif money <= 0:
            lack = input("您的余额不足，请选择 ：1 打开支付宝充值界面 2 退出游戏")
            if lack == "1":
                money += 5000
                print("充值成功，余额为%d" % money)
            elif lack == "2":
                print("欢迎再次游戏")
    elif begin == 2:
        break





