"""
返回值：函数执行结束后，返回给调用处的结果。
    需要使用return关键字，
        1.将结果返回给调用处
        2.结束了方法的执行
"""
import math
# 求和,并将函数的执行结果，给调用处。
# def get_sum(n):
#     sum = 0
#     i = 1
#     while i <= n:
#         sum += i
#         i += 1
#     return sum  # 使用return关键字，将结果返回给调用处
#
#
# # 函数的调用，将函数的计算结果*2打印输出
# res1 = get_sum(10)   # 相当于 res1 = sum
# print(res1 * 2)
#
# # 函数调用，将函数的结果 除以打印输出
# print(get_sum(10) / 2)
#
#
# """
# 练习1：定义一个函数，接收两个参数，用于比较两个数的大小，并将大的数返回。
# 练习2：定义一个函数，用于接收两个参数，求和，并将结果返回。
# """
#
# def get_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# max = get_max(10, 20)
# print(max)
#
#
# def get_add(a, b):
#     return a + b
#
#
# print(get_add(10, 20))
#
#
# # 关于返回值得其他内容
# # 1.如果函数没有返回值
# def fun1():
#     print("我是一个没有返回值得函数。。。")
#
#
# res1 = fun1()  # None
# print(res1)
#
#
# def fun2():
#     print("我也是一个没有返回值的函数。。fun2.。。")
#     return  # 返回结果，并结束方法
#     print("over...")
#
#
# res2 = fun2()
# print(res2)  # None
#
#
# def fun3():
#     i = 0
#     while i <= 10:
#         if i == 5:
#             return  # 强制结束方法，无论方法中有啥
#         print(i)  # 0 1 2 3 4
#         i += 1  # 1 2 3 4 5
#
#
# fun3()
#
#
# def fun4():
#     i = 0
#     while i <= 5:
#         j = 0
#         while j <= 5:
#             if j == 3:
#                 # break
#                 return
#             print(i, j)  # 00, 01,02, 10 ,11,12, 20 21 22..
#             j += 1
#         i += 1
#
#
# fun4()
#
#
# # 2. 函数可以返回的数据类型：数值，字符串，列表，元组。。。
# def fun5_0():
#     list1 = [10, 20, 30]
#     return list1
#
#
# print(fun5_0())
#
# def fun5_1():
#     t1 = (10, 20, 30)
#     return t1
#
# print(fun5_1())
#
# # 如果一个函数返回多个数值，其实本质是以元组的形式返回。建议：
# def fun5_2():
#     return 1, 2, 3  # <class 'tuple'>
#
# print(fun5_2())
# res2 = fun5_2()
# print(res2)
# print(type(res2))
# print(res2[0])
# print(res2[1])
# print(res2[2])
#
# # 序列解包：同时声明多个变量，接收一个函数的返回值
# num1, num2, num3 = fun5_2()
# print(num1)
# print(num2)
# print(num3)
#
# # 课堂练习1：定义一个函数，测量今天的温度和湿度，并返回结果。
# def get_weather():
#     print("开始测量温度。。。")
#     temper = 8.6  # 温度
#     print("开始测量湿度。。。")
#     shidu = 50.2  #
#     return temper, shidu
#
# wendu,shidu =get_weather()
# print("温度%.1f，湿度%.1f" % (wendu,shidu))


"""
练习1：定义一个函数，用于接收一个列表作为参数，判断列表中的每一个年份，是否是闰年，如果是返回

练习2：定义一个函数，接收给定年份，和月份，返回该月的天数。
"""

# data = [2000, 2001, 2002, 2003, 2004, 2017]
#
#
# def is_year(data):
#     num = []
#     for year in data:
#         if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
#             num.append(year)
#     return tuple(num)
#
#
# def get_day(year, month):
#     all_month = (1, 3, 5, 7, 8, 10, 12)
#     day = -1
#     if month == 2:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             day = 29
#         else:
#             day = 28
#     elif month in all_month:
#         day = 31
#     else:
#         day = 30
#     return day
#
#
# print(is_year(data))
#
#
# print(get_day(2017, 12))


def print_line():
    print("-" * 20)


def print_3_line():
    for i in range(1, 4):
        print_line()


print_3_line()


def get_sub(num1, num2, num3):
    """

    :param num1:
    :param num2:
    :param num3:
    :return: 求和
    """
    return num1 + num2 + num3


def get_average(num1, num2, num3):
    """

    :param num1: 数值1
    :param num2: 数值2
    :param num3: 数值3
    :return: 求平均值
    """
    print(get_sub(num1, num2, num3) / 3)


print(get_sub(1, 2, 3))
get_average(1, 2, 3)
