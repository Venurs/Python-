"""
定义一个函数，返回两个数中的最大值

"""


def get_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = int(input("请输入第一个数："))

num2 = int(input("请输入第二个数："))
print(get_max(num1, num2))