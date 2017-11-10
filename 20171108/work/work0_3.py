"""
使用if语句完成：
给定月份，输出该月属于哪个季节。
3,4,5 春季
6,7,8 夏季
9,10,11 秋季
12, 1, 2 冬季
"""

while True:
    month = int(input())
    if 3 <= month <= 5:
        print("春季")
    elif 6 <= month <= 8:
        print("夏季")
    elif 9 <= month <= 11:
        print("秋季")
    elif month == 12 or month == 1 or month ==2:
        print("冬季")
