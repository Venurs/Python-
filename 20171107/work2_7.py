"""
键盘输入年龄，判断年龄是否大于等于18岁
键盘输入两个年龄，小明  小芳年龄  判断两者年龄是否相等
键盘上输入两个两个人的姓名，判断是否相同。
"""
age1 = int(input())
if age1 >= 18:
    print("该年龄大于等于18岁")
else:
    print("该年龄小于18岁")
age_ming = int(input())
age_fang = int(input())
if age_ming == age_fang:
    print("年龄相等")
else:
    print("年龄不相等")
name1 = input()
name2 = input()
if name1 == name2:
    print("姓名相等")
else:
    print("姓名不相等")