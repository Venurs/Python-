"""
埃氏筛法产生素数



问题暂未解决
File "D:/workspace/PythonProject/20171111/exercise/exercise_1.py", line 32, in <module>
    for i in produce_su():
  File "D:/workspace/PythonProject/20171111/exercise/exercise_1.py", line 24, in produce_su
    it = next(num1_list)
"""


# 定义一个数列生成器
# 定义筛选条件
# 定义一个生成器  不断返回下一个素数

# def produce_num():
#     num_list = range(1, 10)
#     return num_list


def choose(n):
    return lambda x: x % n > 0  # lambda 表达式 函数参数：函数体


def produce_su():
    num1_list = range(1, 10)
    count = 0
    while count < 5:
        # 获取数列的第一个值
        it = next(num1_list)
        # filter(函数， 序列)  高阶函数：用函数对序列进行过滤
        num1_list = list(filter(choose(it), num1_list))
        count += 1
    return num1_list

