"""
写一个函数，计算输入的任意两个数之间所有的质数的和
"""
# 判断一个数列中的所有质数


def is_prime(n):
    """
    判断是不是质数
    :param n: 要判断的数
    :return: 无返回值
    """
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    else:
        return True


num1 = int(input("第一个数："))
num2 = int(input("第二个数："))
print(tuple(filter(is_prime, [x for x in range(num1, num2 + 1)])))
print(sum((filter(is_prime, [x for x in range(num1, num2 + 1)]))))


