"""
打印出1-500所有的自然数中不包含4的自然数，共有多少个
"""


def has_four(num):
    string = str(num)
    for i in string:
        if i == "4":
            return True
        else:
            continue


count = 1
cou = 0
while count <= 500:
    if not has_four(count):
        cou += 1
        print(count, end=" ")
    count += 1
print()
print("不含4的个数是：", cou)
