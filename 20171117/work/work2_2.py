"""
2.写一个函数，判断一个数是否是质数
"""


def is_prime(n):
    for i in range(2, (num // 2) + 1):
        if n % i == 0:
            print("不是质数")
            break
    else:
        print("是质数")


num = int(input())
is_prime(num)




