"""
写一个函数，计算输入的任意两个数之间所有的质数的和
"""
# 判断一个数列中的所有质数


def choose(n):
    return lambda x: x % n > 0


def is_prime(n):
    return list(filter(choose(n), list1[1:]))


num1 = int(input())
num2 = int(input())
list1 = [x for x in range(num1 + 1, num2 + 1)]
print(list1)
print(is_prime(list1[0]))
