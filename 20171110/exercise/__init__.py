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

def put():
    if system == 1:
        print("系统出拳，剪刀")
    elif system == 2:
        print("系统出拳，石头")
    elif system == 3:
        print("系统出拳，布")


print("1,剪刀。。2，石头。。3，布。。")
while True:
    system = random.randint(1, 3)
    # print(system)
    play = int(input("请玩家猜拳："))
    if system == play:
        print("平局", end=",")
        put()
    elif (system == 1 and play == 3) or (system == 2 and play == 1) or (system == 3 and play == 2):
        print("系统赢", end=",")
        put()
    elif (system == 3 and play == 1) or (system == 1 and play == 2) or (system == 2 and play == 3):
        print("玩家赢", end=",")
        put()
    elif play > 3 or play < 1:
        print("输入无效,游戏结束")
        break





