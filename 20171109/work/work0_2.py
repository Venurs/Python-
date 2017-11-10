"""
水仙花数,指一个3位数(100-999),每个位上的数值的三次方，
求和，刚好是这个三位数本身。叫水仙花数。4个
"""


def get(num):
    num1 = num // 100
    num = num % 100
    num2 = num // 10
    num = num % 10
    num3 = num
    return num1, num2, num3


count = 100
while count <= 999:
    a, b, c = get(count)
    if a ** 3 + b ** 3 + c ** 3 == count:
        print(count)
    count += 1

