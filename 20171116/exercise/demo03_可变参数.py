"""
可变参数：也叫作不定长参数。其实指的就是参数的个数不确定。
    用于接收多个实参(0-N个)


    语法：* args
    argument

    python中的函数，会将可变参数封装为一个元组来使用。

    1.混合参数：
        位置参数：必须传入实参
        默认值参数：参数名=默认值
        可变参数：*args
            接收0-多个参数--->(元组)

    2.如果传入的时候使用的序列，元组等。实参前*

    3.参数列表中，可变参数只有一个。


"""
def test1(a, b, c):
    pass

def test2(*x):  # 可以同时接收多个参数。。对于函数中x相当于元组。
    print(x)

test2()    # ()
test2(10)  # (10,)
test2(10, 20, 30, 40)  # (10, 20, 30, 40)

"""
tuple:
操作：
    索引，切片
    序列解包：
"""

"""
练习1：设计一个函数，用于接收n个整数求和
练习2：设计一个函数，用于接收n个字符串，并返回拼接后的结果。
"""

def test3(*n):
    # n在函数内部作为元组(1, 2, 3, 4, 5)
    sum = 0
    for i in n:
        sum += i
    return sum

res = test3(1, 2, 3, 4, 5)
print(res)


# sum(),python内置。
list1 = [1, 2, 3, 4, 5]
res2 = sum(list1)
print(res2)

list2 = ["aa", "bb", "memeda"]
# res3 = sum(list2)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(res3)

def test4(*n):
    return sum(n)

print(test4(1,2,3))


def test5(*strs):
    # strs=("hello","二狗","你嘎哈呢")
    # strs= (["hello","二狗","你嘎哈呢"])
    res = ""
    for s in strs:
        res = res + s
    return res


print(test5("hello","二狗","你嘎哈呢"))
list3 = []
while True:
    msg = input("请输入：")
    if msg == "0":
        break
    list3.append(msg)

print(test5(*list3))


print("----------")
# 2.列表中，有位置参数，也有可变参数


def test6(x, *y):
    print("x:", x)
    print("y:", y)


test6(10)
test6(10, 20)
test6(10, 20, 30, 40)

print("------------")
# 3.列表中，有位置参数，有默认值参数，有可变参数
# 位置参数，默认值参数，可变参数。。


def test7(x,y=10,*z):
    print("x:", x)
    print("y:", y)
    print("z:", z)


test7(10)
test7(10, 20)
test7(10, 20, 30, 40)
print("-------")


def test8(x,*z,y=10):
    print("x:", x)
    print("y:", y)
    print("z:", z)


test8(10)
test8(10, 20)
test8(10, 20, 30,40)


def test9(x, *args):
    print("x:", x)
    print("args:", args)


test9(10, 20, 30, 40)
test9(10, *[20, 30, 40])
test9(10, *[1, 2, 3])


def get_sum(*x):
    sum = 0
    for i in x:
        sum += i
    return sum


def string_joint(*x):
    str1 = ""
    for i in x:
        str1 += i
    return str1


print(get_sum(1, 2, 3, 4, 5))

print(string_joint("h", "e", "l", "l", "o"))


