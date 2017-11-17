"""
reduce()规约
    1.python3中，reduce()不再是内置函数，移到functiontools模块
        将一个可以迭代的序列，作用到一个具有两个参数的函数上。
    2.reduce(func,sequence,initial),
        第一个参数：func
            def fun(x, y):
                return 。。。。。

        第二个参数：序列
            [元素1，元素2，元素3.。。。。。]
        第三个参数：初始值
"""
from functools import reduce

def get_sum(a, b):
    return a + b


list1 = [1, 2, 3, 4, 5]
res = reduce(get_sum, list1,0)
print(res)
print(type(res))

res2 = reduce(lambda a, b : a + b, list1, 10)
print(res2)
"""
第一次：
    a = initial
    b = list[0]
    
    a = 0,b = 1
        a + b = 1
        
第二次：
    a = 上次的结果
    b = 列表中的下一个元素
    a = 1, b = 2
        a + b = 3
继续。。
"""

# 阶乘
# 1.函数，2序列，3初始值


print(reduce(lambda a, b: a * b, [x for x in range(1, 11)], 1))


# 练习1：[1,3, 5, 7, 9]--->结果：13579
print(reduce(lambda a, b:  str(a) + str(b), [x for x in range(1, 11)]))
