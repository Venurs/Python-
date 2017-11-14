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
print("----------------5.退出-----------")
while True:
    choose = int(input("请选择："))
    dict1 = dict()
    if choose == 1:
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        qq_number = input("请输入QQ号码：")

    elif choose == 2:
        pass
    elif choose == 3:
        pass
    elif choose == 4:
        pass
    elif choose == 5:
        break




