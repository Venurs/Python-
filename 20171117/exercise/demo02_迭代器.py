"""
迭代器：迭代是访问序列中元素的一种方式。
    依次获取序列中的每一个元组。
        迭代器的工作的过程：
            自动从第一个元素，获取，直到最后。
            只能向后依次获取。

1.可迭代的对象：
    可以直接使用for循环的对象，认为是可迭代的对象。Iterable
        一类数据结构：理解为容器：字符串，列表，元组，字典，集合
        一类是生成器：


2.判断是否可以进行迭代
    导入模块：collections，Iterable


3.迭代器工作：
    迭代器：next()函数来依次获取的数据的对象，迭代器：Iterator
        step1：获取迭代器对象：iter()函数
            iter(可迭代对象)-->迭代器对象it

        step2：依次获取数据：next()
            next(迭代器对象)-->数据，一次获取一个

4.知道迭代器
    总结：
        A：凡是可以使用for循环的遍历的对象，都叫可迭代对象。Iterable
            理解为数据源
        B：凡是可以使用next()依次获取数据对象，都叫迭代器。Iterator
            理解为从数据源获取数据的工具：next()
                step1：iter(可迭代的对象)-->迭代器
                step2：next(迭代器)-->依次获取数据

"""
from collections import Iterable
#1.判断是否可以迭代
s1 = "helloworld"
print(isinstance(s1, Iterable))  # true
num1 = 100
print(isinstance(num1, Iterable))  # False


# 2.使用迭代器遍历字符串
s2 = "abcd"
# step1：获取迭代器对象：iter(s2)
it = iter(s2)
print(it)  # <str_iterator object at 0x0000000000595DD8>
print(type(it))  # <class 'str_iterator'>

# step2：操作迭代器对象获取数据,扩展：迭代器对象.__next__()
print(next(it))  # 获取迭代器可以迭代的第一个元素
print(next(it))
print(next(it))
print(it.__next__())
# print(next(it))  # StopIteration

# step3：for in 遍历
list1 = [1, 2, 3, 4]
it = iter(list1)  # 1,2,3,4
# 循环遍历it
while True:
    try:
        # 尝试获取下一个数据
        x = next(it)
        print(x)
    except StopIteration:
        # 产生异常，结束循环，停止迭代
        break

print("--------")
it2 = iter(list1)  # 1,2,3,4
for x in it2:
    print("-->", x)
