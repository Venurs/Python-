"""
定义一个函数，求两个数的最大公约数
辗转相除法
"""


def min(num1, num2):
    """
    将两数中较大者赋值num1
    :param num1: 数值1
    :param num2: 数值2
    :return: 无返回值
    """
    if num1 < num2:
        num1, num2 = num2, num1


def gcd(num1, num2):
    """
    求两数的最大公约数
    :param num1: 数值1
    :param num2: 数值2
    :return: 最大公约数
    """
    while True:
        if num1 % num2 == 0:
            return num2
        else:
            num2 = num1 % num2
            continue


def lcm(num1, num2):
    """
    求最小公倍数
    :param num1:
    :param num2:
    :return: 最小公倍数
    """
    gcd_number = gcd(num1, num2)
    return num1 * num2 // gcd_number


num1 = int(input("请输入num1："))
num2 = int(input("请输入num2："))
print(gcd(num1, num2))
print(lcm(num1, num2))

