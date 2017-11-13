"""
给定字符串：str="sunjavaandroidjavajavasejavaeejavamec#java.netjavaphpjava",
编写程序，统计字符串"java"出现的次数。多种算法。
"""
# 函数count的使用
str1 = "sunjavaandroidjavajavasejavaeejavamec#java.netjavaphpjava"
print(str1.count("java"))


# 分切
count = sum1 = 0
while count <= len(str1) - 4:
    if "java" == str1[count:count + 4]:
        sum1 += 1
    count += 1
print(sum1)

