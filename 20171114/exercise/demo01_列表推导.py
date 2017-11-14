"""
列表：[元素1，元素2，元素3.。。。]
列表推导：也叫列表包含
    提供了简单的创建列表的方式

语法结构：
    list = [ 表达式 for item in 序列]
"""
# 1.列表推导：产生1-10的数
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [x for x in range(1, 11)]
# print(list1)
# print(list2)

# 2.产生一个列表：0-10的数的立方
# [0,1,8,27,64,125,.... 1000]
# list3 = [x ** 3 for x in range(11)]
# print(list3)
# # 相当于
# list4 = []
# x = 0
# while x < 11:
#     y = x ** 3
#     list4.append(y)
#     x += 1
# print(list4)
"""
练习1：获取1-10的列表
练习2：获取从1-9的平方的列表
练习3：获取从1-9的2倍的列表

"""
# print([x for x in range(11)])
# print([x * x for x in range(10)])
# print([2 * x for x in range(10)])
print([str(i) + "*" + str(j) + "=" + str(i * j) for i in range(1, 10) for j in range(1, 10) if i <= j])
