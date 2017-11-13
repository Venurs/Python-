"""
1.熟练字符串的常用的函数
2.str1 = "hello hello hello world"
    统计字符串的长度
    统计"llo"出现的次数
    统计"wor"出现的位置

3.str2 = "hello"，将字符串长度-->11，左右两边使用-填充
"""

# str1 = "hello hello hello world"
#
# print(len(str1))
# print(str1.count("llo"))
# print(str1.find("wor"))
#
#
# str2 = "hello"
# print(str2.center(12, "-"))


for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("%d*%d=%d" % (i, j, i * j), end=" ")
    print()


