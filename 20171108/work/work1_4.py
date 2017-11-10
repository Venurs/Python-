"""
模拟计算器操作：输入第一个整数，输入第二个整数，输入运算符(+-*/),打印结果
"""
while True:
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    operation = input("请输入你的操作符：")
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
