"""
python中内置的几个高阶函数：
A：列表.sort(key,reverse=False)
    第二个参数：key,函数，用于表示排序的规则
        def sort_rule(x):
            return 数值/字符串
    第三个参数：revers=False，True
B：map()
C：reduce()
D：filter()
"""
# 1.默认排序，升序
# list1 = [1, 6, 2, 5, 4, 3]
# print(list1)
# list1.sort()
# print(list1) # [1, 2, 3, 4, 5, 6]
# list1.sort(reverse=True)
# print(list1)
#
# # 2.可以通过key进行自定义的排序
# list2 = [5, -8, 13, -7, 6, -4]
# # 按照绝对值得，从小到大排序
# list2.sort()
# print(list2)
# list2.sort(key=abs)
# print(list2)
#
# # 3.排序字符串
# list3 = ["apple", "orange", "abc", "helloworld", "zz"]
# list3.sort()  # 默认排序字符串：字符的编码值A:65,B:66..a:97,b:98...
# print(list3)
# 按照字符串的长度排序
# def sort_rule(str1):  # 定义的排序规则
#     return len(str1)
#
#
# list3.sort(key=sort_rule)
# print(list3)
#
# list3.sort(key=sort_rule, reverse=True)
# print(list3)



"""
练习1：将给定的列表中的字符串，忽略大小写排序


练习2：给定一个字典：按照年龄排序从小到大
students = [
    {
        "name": "王二狗",
        "age": 18,
        "score": 88
    },
    {
        "name": "三胖",
        "age": 19,
        "score": 58
    },
    {
        "name": "李小花",
        "age": 25,
        "score": 98
    }
]
"""
list4 = ["bob", "Rose", "Tom", "jerry", "Jack"]
students = [
    {
        "name": "王二狗",

        "score": 0,
        "age": 18
    },
    {
        "name": "三胖",

        "score": 99,
        "age": 9
    },
    {
        "name": "李小花",

        "score": 98,
        "age": 25
    }
]

print(sorted(list4, key=str.lower))

list4.sort(key=str.lower)
print(list4)

# sorted:排序后产生一个新的序列
# sort：在原序列的基础上进行排序，排序后改变原有序列顺序。
print(sorted(students, key=lambda i: i["age"], reverse=True))
students.sort(key=lambda i: i["age"])
print(students)

