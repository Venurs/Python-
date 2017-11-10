"""
求给定的年份，是否是闰年。

满足以下两点中任意一点就是闰年

A：能被4整除，但是不能被100整出。

B：能被400整除。
"""
while True:
    year = int(input("请输入年份："))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("是闰年")
    else:
        print("不是闰年")
