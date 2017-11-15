"""
6.定义一个函数，用于求2017年1月到month前一个月的总天数
"""


def days(month):
    day_big = (1, 3, 5, 7, 8, 10, 12)
    day_small = (4, 6, 9, 11)
    day = 0
    for i in range(1, month + 1):
        if i in day_big:
            day += 31
        elif i in day_small:
            day += 30
        elif i == 2:
            day += 28
    return day


month = int(input("请输入截至月份："))
print(days(month))
