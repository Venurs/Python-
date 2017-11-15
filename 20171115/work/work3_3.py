"""
将学生管理系统，改为函数版。
"""


def choose1():
    name_student = input("请输入学生姓名：")
    age_student = int(input("请输入学生年龄："))
    qq_number_student = input("请输入QQ号码：")
    student.append(dict(name=name_student, age=age_student, qq_number=qq_number_student))
    print("添加成功")


def choose2():
    name_student = input("请输入要删除的学生的名字：")
    for stu in student:
        if stu["name"] == name_student:
            student.remove(stu)
            print("删除成功")
    else:
        print("该学生不存在。。。。")


def choose3():
    name_student = input("请输入要修改的学生的姓名：")
    print("1.修改姓名")
    print("2.修改年龄")
    print("3.修改QQ号码")
    select = int(input("请输入要修改的信息编号："))
    for stu in student:
        if stu["name"] == name_student:
            if select == 1:
                new_name = input("请输入新名字：")
                stu["name"] = new_name
            elif select == 2:
                new_age = int(input("请输入新的年龄："))
                stu["age"] = new_age
            elif select == 3:
                new_qq = input("请输入新的QQ号码：")
                stu["qq_number"] = new_qq
        print("修改成功")


def choose4():
    name_student = input("请输入要查找的学生的名字：")
    for stu in student:
        if stu["name"] == name_student:
            print(stu)


def choose5():
    for stu in student:
        print(stu)


print("------------------欢迎来到学生管理同学---------------")
print("----------------请选择一下操作中的任意一项-----------")
print("----------------1.添加学生-----------")
print("----------------2.删除学生-----------")
print("----------------3.修改学生-----------")
print("----------------4查找学生-----------")
print("----------------5.查看所有学生-----------")
print("----------------6.退出-----------")
student = []
while True:
    choose = int(input("请选择："))
    if choose == 1:
        choose1()
    elif choose == 2:
        choose2()
    elif choose == 3:
        choose3()
    elif choose == 4:
        choose4()
    elif choose == 5:
        choose5()
    elif choose == 6:
        print("系统退出")
        break