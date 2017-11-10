"""
统计1月-5月的总天数。
"""

year = int(input("请输入年份："))
count = 1
day = 0
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

    while count <= 5:
        if count == 2:
            day += 28
        elif count % 2 == 0:
            day += 30
        elif count % 2 != 0:
            day += 31
    print(day)
else:
    # count = 1
    # day = 0
    while count <= 5:
        if count == 2:
            day += 29
        elif count % 2 == 0:
            day += 30
        elif count % 2 != 0:
            day += 31
    print(day)
