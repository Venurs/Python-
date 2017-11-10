"""
键盘输入一个四位数的整数，分别获取各个位数的值
"""
number = int(input("请输入一个四位数："))
print(int(number / 1000))
number = number % 1000
print(int(number / 100))
number = number % 100
print(int(number / 10))
number = number % 10
print(number)
