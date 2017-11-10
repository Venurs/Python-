"""
练习1：设计两个整数，比较大小，以及是否等于
练习2：声明2个变量：姓名，年龄。。判断结果：姓名是否王二狗，并且年龄是不是大于23岁
练习3：声明2个变量：性别，年龄。。判断结果，如果是女生，或者大于30岁
"""
# num = int(input())
# if num < 0:
#     print(-1 * num)
# else:
#     print(num)
#
#
# age = int(input("请输入年龄"))
# if age > 22:
#     print("可以娶媳妇了")
#
#
# score = int(input("请输入成绩"))
# if score >= 60:
#     print("及格")
#
#
# number = int(input("请输入数字"))
# if number > 0:
#     print("正数")

# while True:
#     num = int(input())
#     if num == 0:
#         print("光头强")
#     elif num == 1:
#         print("熊大")
#     elif num == 2:
#         print("熊二")
#     elif num == 3:
#         print("熊三")
#     elif num == 4:
#         print("熊四")
#
# lan = input()
# if lan == "思密达":
#     print("韩语")
# elif lan == "么么哒":
#     print("汉语")
# elif lan == "八格牙路":
#     print("日语")
#

# while True:
#     num = int(input())
#     if num >= 90:
#         print("优秀")
#     elif num >= 80:
#         print("良好")
#     elif num >= 70:
#         print("中等")
#     elif num >= 60:
#         print("及格")
#     elif num < 60:
#         print("不及格")

count = 1
sum3 = 0
while count <= 100:
    sum3 += count
    count += 1
print(sum3)


count = sum1 = 1
while count <= 5:
    sum1 *= count
    count += 1
print(sum1)


count = 58
while count >= 23:
    print(count, end=" ")
    count -= 1

print()

count = sum2 = 1
while count <= 100:
    print(count, end=" ")
    if (count + 1) % 20 == 0:
        print()
    count += 2




