"""
字典：key:value，名值对的组合。无序
    1.增加：
        字典名["key"] = value
    2.删除：根据键，删除键值对
        pop(key)
        del 字典名["key"]
    3.修改：key已经存在，就是修改，不存在就是添加
        字典名["key"] = value
    4.查找：也就是获取
        根据key获取对应的值
        字典名["key"]-->value，如果key不存在，报错KeyError: 'address'
        字典名.get(key)-->value,如果key不存在，返回None

补充：
    in，not in
    keys()-->该字典中所有的key组成的序列，使用for ...in 遍历
    values()--->获取字典中所有的value。
    items()--->获取名值对的组合
"""
# print("1.字典元素的获取---------------")
# person1 = {
#     "name": "王二狗",
#     "age": 30,
#     "sex": "男"
# }
# print(person1)
# print(person1["name"])
# print(person1["sex"])
# # print(person1["address"])  # KeyError: 'address'
# print(person1.get("sex"))
# print(person1.get("address"))
#
# print("2.字典元素的增加---------------------")
# person1["address"] = "北京市"
# print(person1)
# person1["address"] = "上海市"
# print(person1)
#
# print("3.删除---------------")
# person1.pop("name")
# print(person1)
# del person1["sex"]
# print(person1)
#
# if "QQ" in person1:
#     print(person1["QQ"])
# else:
#     print("没有该数据。。")
#     person1["QQ"] = "10086"
#
# print(person1)
#
# if "QQ" in person1:
#     print(person1["QQ"])
# else:
#     print("没有该数据。。")
#     person1["QQ"] = "10086"
#
#
# print("------")
#
# print(len(person1))  #
# # 获取所有的key
# for key in person1.keys():
#     # print(key, person1[key])
#     print(key, person1.get(key))
#
# # 获取所有的值
# # print(person1.values())
# for value in person1.values():
#     print(value)
#
# # 获取名值对
# # print(person1.items())
# for item in person1.items():
#     # print(item)
#     print(item[0], item[1])

"""
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

"""
练习1：创建空字典，添加3个名值对
练习2：修改某一个key对应的值
练习3：删除某两个key
"""


dict1 = dict()
dict1["name"] = "二傻子"
dict1["age"] = "22"
dict1["sex"] = "男"
print(dict1)
dict1["age"] = 21
print(dict1)
# dict1.pop("age")
# dict1.pop("sex")
print(dict1)
print(dict1.items())
print(dict1.keys())

