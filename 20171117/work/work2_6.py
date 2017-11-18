"""
传入多个参数，以list返回
"""


def return_list(*k):
    list1 = [x for x in k]
    return list1


print(return_list(1, 2, 3, 4, 5, 6, 7))

