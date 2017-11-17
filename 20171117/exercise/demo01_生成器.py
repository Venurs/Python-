"""
一。列表推导，用于快速的产生一个列表。(列表生成式)
    list = [表达式 for x in 范围]
           [表达式 for x in 范围 if 条件]
           [表达式 for x in 范围 for y in 范围]

    满足该公式，所有范围的数--->列表中
        内存中：列表推导范围较大，一次性产生所有的数据存入了列中

二。生成器(generator)
    生成器：在python中，一边循环，一边产生数据，就叫做生成器。
        理解：按照某种规则，产生数据。

    方法一：只要把列表推导的[],改成()，就获得一个generator。
    方法二：使用函数，使用yield关键字，那么该函数就是是一个生成器
        def 函数名():
            ..
            yield 生成的数据

"""
# 1.列表推导
# range(start,end,step)-->范围的数据：[start,end)
# 产生1-10的列表
list1 = [x for x in range(1, 11)]
print(list1)
# 产生1-10的平方的列表
list2 = [x ** 2 for x in range(1, 11)]
print(list2)
# 产生0-20的偶数的列表
list3 = [x for x in range(21) if x % 2 == 0]
print(list3)

# 使用循环
list4 = [int(str(x)+str(y)) for x in range(1, 10) for y in range(0, 10)]
print(list4) # 10,11,12,13..19,20,21,22...29,30.31....99
list5 = [x * 10 +y for x in range(1, 10) for y in range(0,10)]
print(list5)
"""
for x in range(1, 10):
    for y in range(0, 10):
        res = str(x)+str(y)
        print(res)
"""

print("------------------")
# 2.使用生成器：创建生成器，方法一：[]-->()
# 产生1-10的列表
list1 = [x for x in range(1, 11)]  # 得到的是列表
gen1 = (x for x in range(1, 5))  # 得到是生成器的对象
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(gen1)  # <generator object <genexpr> at 0x00000000021CAD38>

print(type(list1))  # <class 'list'>
print(type(gen1))  # <class 'generator'>

# 根据生成器对象，获取数据
"""
生成器的使用：
step1：创建生成器对象：(公式 for x in 范围)-->generator
    能够产生[1,2,3,4]
    一个生成器：
        next(),for循环
step2：获取生成器产生的数据
    调用next(生成器对象)-->
"""
print(next(gen1))  # 根据生成器获取生成的第一个数
print(next(gen1))  # 同上，获取第二个数。。
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))  # StopIteration，生成器中已经没有数据可以产生，抛出异常
for x in gen1:
    print("-->",x)


"""
练习1：使用生成器，获取1-10的平方的列表。
        获取前5个。
"""
print("-------------")
# 方法二：使用函数，产生一个生成器
# step1：定义一个函数


def foo(n):  # 打印1-n的数字
    print("------start------")
    for i in range(1, n+1):
        # print(i)
        yield i  # 每次执行到yield，在次数暂停，并且记住下次
    print("------end-------")

# foo(5)  # 暂时不执行

# step2：根据带有yield关键字的函数，获取对应的生成器
gen2 = foo(5)

# step3：根据生成器产生数据
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
# print(next(gen2))

"""
难点：关于生成器函数的执行过程
    变成了生成器的函数，在每次next()函数调用的时候，执行，遇到yiled 返回结果，并暂停。直到下次调用next()
"""
"""
练习1：使用函数生成器，产生数字：1-10的奇数
练习2：使用函数生成器，产生斐波那契数列：
"""
"""
兔子
"""
print("----------------")


def fob(n):
    a = 1
    b = 0
    c = 0
    for x in range(1, n + 1):
        c = a + b
        yield c
        a = b
        b = c
    return c


gen = fob(10)
for x in gen:
    print(x, end=" ")

print()
print("----------------")


def number(n):
    for x in range(1, n + 1, 2):
        yield x


gen = number(5)
print(next(gen))
# for i in gen:
#     print(i, end=" ")


