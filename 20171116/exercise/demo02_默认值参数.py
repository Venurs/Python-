"""
默认值参数：
    1.概念：定义一个函数的时候，直接给形参赋值，叫做默认值参数

    2.语法：
        def 函数名(参数="默认值")

    3.默认值参数的赋值时机：
        在函数定义的时候。

    4.参数的默认值，也可以是函数。(了解)

    5.注意点：
        A：如果一个函数中参数，使用默认值参数，那么该默认值参数后的参数也是默认值参数，否则报错。
        B：如果默认值参数是列表，字典。函数中操作该列表或字典，一直是同一个。除非使用实参进行覆盖。
"""

def test1(a, b='x'):
    print("a:", a)
    print("b:", b)
    print("over....")


test1(10, 20) # 如果传入了实参，就不使用默认值参数。
test1(100)  # 默认值参数，如果没有传入实参，就使用默认值

print("------------")
i = 10  # 全局变量
def test2(x, y=i):  # test2()函数的声明：如果默认值参数，就已经赋值了
    print("x:",x)
    print("y:",y)
    print("over...")

i = 20  # 修改全局变量i的数值，不会影响默认值。
print(i)
test2(100)

print("------------------")
# 默认值参数，也可以是一个函数的返回值
def foo(x=10):
    return x

print(foo())
print(foo(100))

def test3(x=foo(20), y=foo()):
    print(x)
    print(y)
    print("******")

test3()  # 20 10
test3("a", "b")  # a,b
test3("a")  # a 10


print("------------")
# def test4(a, b=10, c):  # 使用规则：默认值参数后的参数也是默认值参数
#     pass

def test5(x, y=[]):  # y = []
    y.append(x)
    print(y)

test5(10)
test5(20)
test5(30,[])

list1 = []
list2 = []

"""
默认值参数语法：
"""
list1 = [1, 5, 3, 4, 2]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)