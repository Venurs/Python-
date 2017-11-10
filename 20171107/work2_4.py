"""
键盘上输入两个整数，比较两个数的关系是否大于，是否小于，是否等于，是否不等于
"""
number1 = int(input("请输入第一个数："))
number2 = int(input("请输入第二个数："))
if number1 > number2:
    print("大于")
elif number1 == number2:
    print("等于")
else:
    print("小于")
