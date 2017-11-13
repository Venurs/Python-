"""
字符串的常用方法：
A：字符串大小写
capitalize(),字符串首字母大写
title(),标题化，每个单词首字母大写
upper(),大写
lower(),小写
swapcase(),交换

B：对齐
center(width,fillchar),填充
strip(chars),去除首尾的指定内容，如果不传入参数，去除的是空格
lstrip(),rstrip()


C：查找
s1.find(sub,startindex,endindex),查找子串，返回值是下标，如果不存在返回-1
s1.index(sub,startindex,endindex),查找子串，返回值就是下标，如果不存在，报错：ValueError: substring not found
in，not in-->查找子串，返回值是bool。


D：判断
isalpha(),是否是字母
isalnum(),是否是字母和数字
isdigit(),是否是数字

E：
split(chars,maxsplit),切割,按照指定的字符切割，将切割后的元素存入到一个列表中
    maxsplit：指定了切割的最大数量

s1.count(sub),获取sub在s1中出现的次数


"""
s1 = "liFE is shORt"
print(s1)
print(s1.capitalize())  # 首字母大写，整个字符串首字母大写
print(s1.title())  # 标题化，每个单词首字母大写

print(s1.upper())
print(s1.lower())
print(s1.swapcase())  # 交换大小写：原来大写，转小写，原来小写，转为大写

print("-"*50)
s2 = "hello"
print(s2)
print(s2.center(10))
print(s2.center(10, "*"))


s3 = "hello world"
"""
s1.find(sub)
    在字符串s1中查找子串sub，
        如果存在，那么返回位置下标
        如果不存在，返回-1。
"""
print(s3.find("ll", 5))

# print(s3.index("lll"))  # ValueError: substring not found


print(s3.isalpha())  # 判断是否全部都是字母
s4 = "hello123_"
print(s4.isalnum())  # 判断是否是数字和字母5
s5 = "100"
print(s5.isdigit())


s6 = "   hello world    "
print(s6)
print(s6.strip())
s7 = "**hello world******"
print(s7.strip("*"))
print(s7.lstrip("*"))
print(s7.rstrip("*"))

print("----------")
s8 = "ab-ccc-d-h-uu-p-ll"
print(s8.split("-"))  # ['ab', 'ccc', 'd', 'h'],列表
print(s8.split("-", 2))
print(s8.split("-", 3))

s9 = "hello王二狗pythonaaapython123pythonaixuexipython"
print(s9.count("pythonn"))