"""
列表的常用操作：
    1.列表中的增删改查
        A：增加元素
            a)append(元素),追加，末尾添加
            b)insert(index，元素),指定位置添加

        B：删除
            a)pop(),默认，获取最后一个元素
            b)pop(index),删除指定位置的元素
            c)remove(元素),根据元素删除
            d)del ,扩展内容：del 列表[index]

        C：修改
            列表名[index] = 新值

        D：查找
            列表[index]


    2.列表的合并
        A：+
            列表1 + 列表2 = 列表3
        B：extend,词义：扩展
            列表1.extend(列表2)-->列表3


"""
# # 1.定义列表
# names1 = ["王二狗", "李小花", "三胖"]
# names2 = [ "Rose", "Jack", "Tom", "Jerry"]
#
# # 2.增加元素
# print(names1)
# names1.append("啸天")
# print(names1)
# names1.insert(2, "隔壁老王")
# print(names1)
#
# # 3.修改
# print(names1)
# names1[1] = "李如花"
# print(names1)
#
#
#
#
# print("-"*50)
# # 4.删除元素
# names1.pop()
# print(names1)
# names1.pop(1)
# print(names1)
#
# names1.remove("王二狗")  # ValueError: list.remove(x): x not in list
# print(names1)
#
# del names1[1]
# print(names1)
#
#
# print("-"*50)
# names1 = ["王二狗", "李小花", "三胖"]
# names2 = [ "Rose", "Jack", "Tom", "Jerry"]
# names3 = names1 + names2
# print(names1)
# print(names2)
# print(names3)
#
# print("---------")
# # names1.append(names2)
# names1.extend(names2)
# print(names1)
# print(names2)
# print(len(names1))


"""
名字管理练习：1701班所有的学生姓名
    1.查找学生姓名
        "王二狗"
    2.增加学生姓名
        "李雪"
    3.修改学生姓名
        "王旺旺"
    4.删除学生姓名
        ""
"""
student = ["史光大", "曲义龙", "王立威"]
while True:
    choose = int(input("请输入操作："))

    print("姓名列表：", end=" ")
    print(len(student))

    for i in student:
        print(i)
    if choose == 2:
        name = input("请输入要添加的名字：")
        student.append(name)
        print("添加成功")
    elif choose == 1:
        name = input("请输入要查找的名字：")
        if name in student:
            print("该姓名存在")
        else:
            print("不存在")
    elif choose == 3:
        name = input("请输入要修改的名字：")
        name_new = input("请输入要新修改的名字：")
        for i in student:
            if i == name:
                i = name_new
                print("成功")
            else:
                continue
    elif choose == 4:
        name = input("请输入要删除的名字：")
        student.remove(name)
        print("删除成功")




