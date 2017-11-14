"""
使用字典：学生管理系统
学生姓名管理系统：
    names_list = ["王二狗", "Rose", "Jack" ...]
    增加学生姓名，删除，修改，查找。。
        append(),
        pop(index),remove(元素)
        name_list[index] = 新值

字典：存储一组信息
    names_list = [
        {
            "name": "王二狗",
            "age" : 18,
            "QQ": "1234567"
        },
        {
            "name":"Rose",
            "age":19,
            "QQ":"567878"
        },
        .....
    ]


        新增学生信息：

            创建字典：stu_dict = {}
                接收姓名，年龄，QQ
                    stu_dict["name"] = 姓名
                    stu_dict["age"] = 18
                    stu_dict["QQ"] = "12345"
            names_list.append(stu_dict)

            删除：del_name = "王二狗"

            修改：

            查找：
"""


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
        name_student = input("请输入学生姓名：")
        age_student = int(input("请输入学生年龄："))
        qq_number_student = input("请输入QQ号码：")
        student.append(dict(name=name_student, age=age_student, qq_number=qq_number_student))
        print("添加成功")
    elif choose == 2:
        name_student = input("请输入要删除的学生的名字：")
        for stu in student:
            if stu["name"] == name_student:
                print(type(stu))
                student.remove(stu)
                print("删除成功")
    elif choose == 3:
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
    elif choose == 4:
        name_student = input("请输入要查找的学生的名字：")
        for stu in student:
            if stu["name"] == name_student:
                print(stu)
    elif choose == 5:
        for stu in student:
            print(stu)
    elif choose == 6:
        print("系统退出")
        break




