"""
元组：(tuple),与列表(list)类似,都是用于存储一组数据。
    和列表的区别：
        1.列表的内容是允许修改。但是元组一旦创建，内容不能修改
    2.列表：[],元组：使用()，

元组的使用：
    A：元组的创建：
        ()直接创建
        tuple(序列)-->

    B：元组的操作：
        索引：tuple[index]
        切片：tuple[start:end]

    切记：元组一旦创建不能修改。
"""
# list1 = [10, 20, 30]  # <class 'list'>
# tuple1 = (10, 20, 30)  # <class 'tuple'>
# print(list1)
# print(tuple1)
# print(type(list1))
# print(type(tuple1))
#
# # 创建元组：元组创建时，括号可以省略，但是不建议
# tuple2 = 10, 20, 30  # tuple2 = (10, 20, 30)
#
# tuple3 = 10,  # tuple3 = (10,)
#
#
# print(tuple2)
# print(tuple3)
#
# tuple4 = (10)  # 会被python解释器认为是一个整形变量
# print(tuple4)
# print(type(tuple4))
#
# tuple5 = ()  # 创建了一个空的元组

# 通过元组的构造来创建：tuple(序列)
# list2 = [10, 20, 30, 40]
# tuple6 = tuple(list2)
# print(tuple6)


# 获取元组中的数据
# t1 = ("王二狗", 18, "男", "北京市冒烟儿胡同XX路")
# print(t1)
# # 获取第一个
# print(t1[0])
# print(t1[3])
#
# print(len(t1))
#
# # 遍历元组：for in，while
# index = 0
# while index < len(t1):
#     print(t1[index])
#     index += 1
#
# print("-" * 50)
# for i in t1:
#     print(i)
#
# print("-" * 50)
# 元组不允许修改
# t1[0] = "王二狗狗"  # TypeError: 'tuple' object does not support item assignment
# print(t1)
# print(t1[0:2])

"""
练习1：创建元组
练习2：元组的索引和切片
练习3：元组嵌套列表。
"""

tuple1 = (1, 2, 3, 4)
for i in tuple1:
    print(i, end=" ")
    print(tuple1[0:2])
tuple2 = ([1, 2, 3], [4, 5, 6], (9, 8))
print(tuple2)
