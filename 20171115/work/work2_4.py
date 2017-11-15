"""
定义一个函数，求1-n的范围内，偶数的和
"""


def sum_even(n):
    sum = 0
    for i in range(2, n + 1, 2):
        sum = sum + i
    return sum


number = int(input("请输入最大范围值："))
print(sum_even(number))

