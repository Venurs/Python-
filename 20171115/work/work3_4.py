import time
"""
菲波那切数列
"""


def Fiboone(i):
    """
    递归产生菲波那切数列
    :param i: 数列的第i个
    :return:
    """
    if i == 1 or i == 2:
        return 1
    else:
        return Fiboone(i - 1) + Fiboone(i - 2)


start = time.clock()
value = int(input("请输入序列的个数："))
for i in range(1, value + 1):
    print(Fiboone(i), end=" ")
# num = []
#
# for i in range(value + 1):
#     if i == 0 or i == 1:
#         num.append(1)
#     else:
#         num.append(num[i - 1] + num[i - 2])

# print(num)

end = time.clock()
print("代码运行时间为", end - start)


