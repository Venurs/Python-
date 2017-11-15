"""
定义一个函数，通过参数，接收三角形边长，打印三角形
"""


def print_trigon(w):
    for i in range(1, w + 1):
        for j in range(1, i + 1):
            if i >= j:
                print("*", end="")
        print()


w = int(input("输入一个数:"))
print_trigon(w)
