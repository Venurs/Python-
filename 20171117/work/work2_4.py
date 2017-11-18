"""
定义函数，输入一个日期，判断该日期是今年的第几天。例如输入2016-01-01打印第1天
function which_day (year, month, day)
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


def months(month):
    """
    返回传入月份之前的所有月份
    :param month:
    :return: 月份列表
    """
    month_list = [mon for mon in range(1, month + 1)]
    return month_list


def days(year, month, day):
    """
    求总天数
    :param month:
    :param day:
    :return: 返回总天数
    """
    list1 = months(month)
    big_month = [1, 3, 5, 7, 8, 10, 12]
    small_month = [4, 6, 9, 11]
    sum_day = day
    list1.pop(len(list1) - 1)
    for i in list1:
        if i == 2:
            if leap_year(year):
                sum_day += 28
            else:
                sum_day += 29
        elif i in big_month:
            sum_day += 31
        elif i in small_month:
            sum_day += 30
    return sum_day


year = int(input("年："))
month = int(input("月："))
day = int(input("日："))
print("第%d天" % days(year, month, day))
