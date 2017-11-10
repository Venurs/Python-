"""
给定3个整数，从小到大输出
"""
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
num3 = int(input("请输入第三个数："))
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2
print(num1, num2, num3)
