"""
遍历字符串

给定字符串"abdefghigk",使用for...in循环查找字母c并输出，如果没有就打印没有找到

"""


# s1 = "wo te me de zhen kun"
# for i in s1:
#     print(i, end=" ")
#
#
# print()
# s2 = "abdefghcccigk"
# for i in s2:
#     if i == "c":
#         print(i)
#         continue
# else:
#     print("没有找到")


# 切片

"""
课堂练习：
s4 = "0123456789"
课堂练习：
1截取下标是从2到5 的字符串
2截取下标从2开始到末尾的字符串
3截取字符串开始到5 的位置，不包含5
4截取完整的字符串
5从开始位置，每隔一个字符截取
6从索引1开始，每隔一个字符截取
7截取从2 到末尾的前一个字符
8截取末尾2个字符串
9 思考，如何反转字符串
"""

s4 = "0123456789"
print(s4[2:6])
print(s4[2:])
print(s4[:5])
print(s4[:])
print(s4[::2])
print(s4[1::2])
print(s4[2:-1])
print(s4[-2:])
print(s4[-1::-1])




