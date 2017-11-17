"""
函数操作变量的规则：
    函数中只能够修改局部变量， 不能修改全局变量。全局变量对于函数来讲，是"只读"的。
        函数内部为某个全局变量重新赋值：相当于在函数内部重新定义了该变量。而不是修改全局变量的数值。

局部变量a
def outer1():
    外层函数变量a
    a = ""
    def inner1():
        里层函数变量a
        a = ""

"""
# 1.定义一个全局变量
a = 10
print(a)

def foo():
    print(a)

foo()

def foo2():
    a = 20  # 这里其实是 新定义了局部变量a，只是和全局变量a重名。并不是修改全局变量。
    print(a)

foo2()
print(a)


def foo3():
    # a = a + 2  # a没有初始值。
    print(a)


print("-----------")
a = "我是一个全局的A"
print(a)

def foo4():
    a = "重新定义一个外层的变量a"  # 重新定义变量a
    print(a)

    def foo4_in():
        a = "内层函数的变量a"  # 也是重新定义了里层函数的a，不是修改外层函数的a
        print(a)
    foo4_in()
    print("-->", a)


foo4()
print(a)

