"""
函数的参数：
    形式参数：形参
        声明函数的时候，（）里面的参数，本质就是一个变量
        形参就是一个变量：变量的数值对于函数来讲不确定。由调用处来确定。
    实际参数：实参
        函数调用的时候，传递给形参的具体的数值，就叫做实参。


函数的调用：
    A：函数名对应
    B：实参匹配形参：
        如果一个函数有参数，那么调用的时候要传入相应的数值。
def 函数([形参列表])
"""
# 1.定义函数,求1-n的和
# def get_sum(n):
#     i = 1
#     sum = 0
#     while i <= n:
#         sum += i
#         i += 1
#     print("1-%d的和：%d" % (n,sum))
#
#
# # 1,求1-10的和
# get_sum(10)
#
# # 2.求1-20的和
# get_sum(20)
#
# # 3.求1-100的和
# get_sum(100)


"""
1.定义一个方法：求n的阶乘。调用的时候，由键盘输入。
2.定义一个方法：求2个数的和。2个数由参数传入。。
"""


def factoriall(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    print(res)


def print_san(num1, num2):
    return num1 + num2


n = int(input())
factoriall(n)

num1 = int(input())
num2 = int(input())
print(print_san(num1, num2))
