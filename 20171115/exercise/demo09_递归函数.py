"""
递归函数：
    函数调用自己。

    注意：
        1.要有出口
        2.逐渐的像出口靠近
例：求1-5的和
定义一个函数，用于求1-n的和。get_sum(n)
n = 5,get_sum(5),求1-5 的和
1-4的和，加5
n = 4,get_sum(4),求1-4的和
    get_sum(5) = get_sum(4) + 5
n = 3,get_sum(3)，求1-3 的和
    get_sum(4) = get_sum(3) + 4

n = 2,get_sum(2),求1-2 的和
    get_sum(3) = get_sum(2) + 3

n = 1,get_sum(1),就是1
    get_sum(2) = get_sum(1) + 2

    get_sum(1) = 1

"""
# def get_sum(n):
#     print("*******")
#     if n == 1:
#         return 1
#     else:
#         return get_sum(n-1) + n


# res = get_sum(5)
# print(res)
#
#
# print("-------")

# 求n的阶乘


def get_sum(n):
    print("*******")
    if n == 1:
        return 1
    else:
        return get_sum(n-1) * n


print(get_sum(5))

