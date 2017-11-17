"""
关键字参数：调用函数的时候实参赋值给形参，调用时写清楚形参的名字
"""
def test1(a,*b,c):
    print("a:",a)
    print("b:",b)
    print("c:",c)

test1(10,20,30,c=40)

print("么么哒", end="")  # 关键字参数

print("------")
# 默认值参数
def test2(x=10, y=20, z=30):
    print("x:" ,x)
    print("y:", y)
    print("z:", z)

test2()
test2("a")
test2(z="a")
test2(y="b", z="a")
# test2(a=1,b=2)  # 关键字参数的参数名，需要和形参匹配上。

# 如果传入的实际的关键字参数和形参列表对应不上，使用**kw(keyword),接收之后封装字典
def test3(name="王二狗",age=30,**kw):
    print("name:", name)
    print("age:", age)
    print("kw:", kw)

test3("李小花",age=18,sex="女",country="中国")