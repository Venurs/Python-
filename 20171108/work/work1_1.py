"""
age = ...;

sex = ...;

如果age>18，并且 sex为false，

输出“女大十八变。。。。。”
"""
while True:
    age = int(input("请输入年龄："))
    sex = input("请输入性别：")
    if age > 18 and sex == "false":
        print("女大十八变。。。。。")

