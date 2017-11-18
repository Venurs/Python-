"""定义函数，输入一个日期，判断该日期是否合法；
例如：输入 2015, 2, 29不合法。
function is_date (year, month, day)
"""

def leap_year(year):
    """
    判断是不是闰年
    :param year: 年份
    :return: 是闰年，返回True
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def judge_date(year, month, day):
    big_month = [1, 3, 5, 7, 8, 10, 12]
    small_month = [4, 6, 9, 11]
    if month in range(1, 13):
        if month == 2 and day in range(1, 29) and leap_year(year):
            print("日期合法")
        elif month == 2 and day in range(1, 30) and (not leap_year(year)):
            print("日期合法")
        elif month in big_month and day in range(1, 32):
            print("日期合法")
        elif month in small_month and day in range(1, 31):
            print("日期合法")
        else:
            print("日期不合法")
    else:
        print("日期不合法")


year = int(input("年："))
month = int(input("月："))
day = int(input("日："))
judge_date(year, month, day)
