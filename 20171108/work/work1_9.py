"""
统计1月-12月，奇数月的总天数。
1月+3月+5月。。。11月
"""
month = 1
day = 0
while month <= 12:
    if month == 9 or month == 11:
        day += 30
    else:
        day += 31
    month += 2
print(day)
