"""
1.万年历
1900年1月1日，星期一
星期一	星期二	星期三	星期四	星期五	星期六	星期日
1	2	3	4	5	6	7
8	9	10	11	12	13	14
15	16	17	18	19	20	21
22	23	24	25	26	27	28
29	30	31	1	2	3	4
5	6	7	8	9	10	11
31-28=3
1900年2月的日期

2017年11月的日历
2017年10月30日距离1900年1月1日的总天数
除以7，取余数，就是空格数
1900年，2016年：
365,366

2017年：1月-10月的总天数
"""


def judge_month(year, month):
    """
    求指定年份的指定月份的天数
    :param year:指定年份
    :param month: 指定月份
    :return: 返回天数
    """
    big_month = [1, 3, 5, 7, 8, 10, 12]
    small_month = [4, 6, 9, 11]
    day = -1
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            day = 29
        else:
            day = 28
    elif month in big_month:
        day = 31
    elif month in small_month:
        day = 30
    return day


def now_days(year, month):
    """
    返回指定年的到指定月为止的总天数
    :param year:指定年
    :param month:指定月
    :return:总天数
    """
    big_month = [1, 3, 5, 7, 8, 10, 12]
    small_month = [4, 6, 9, 11]
    sum_day = 0
    for i in range(1, month):
        if i == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                sum_day += 29
            else:
                sum_day += 28
        elif i in big_month:
            sum_day += 31
        elif i in small_month:
            sum_day += 30
    return sum_day


def judge_year(years, month):
    """
    累计1900年到指定年指定月的总天数
    :param years: 指定年
    :param month: 指定月
    :return: 返回总天数
    """
    days = now_days(years, month)
    for year in range(1900, years):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days += 366
        else:
            days += 365
    return days


def week(years, month):
    """
    将指定年份的指定月份放入一个列表，第一天之前不满一周的天数用空格代替
    :param years:
    :param month:
    :return:
    """
    days = judge_year(years, month)
    # week = days + judge_month(years, month)
    week_list = list()
    which_day = days % 7
    for j in range(0, which_day):
        week_list.append(" ")
    for i in range(1, judge_month(years, month) + 1):
        week_list.append(i)
    return week_list


year = int(input("年："))
month = int(input("月："))
list1 = week(year, month)
print("星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t星期天")
for i in range(0, len(list1)):
    print(list1[i], end="\t\t")
    if (i + 1) % 7 == 0:
        print()


