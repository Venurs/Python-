"""
定义一个函数，求一个数的绝对值
"""


def absolute(value):
    if value < 0:
        return -1 * value
    return value


value = int(input("请输入一个数："))
print(absolute(value))

