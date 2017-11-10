"""
键盘上输入1-5个数字，
分别代表
1:特遣队列表\n
2:添加特遣队成员\n
3:删除特遣队成员\n
4:修改特遣队成员\n
5:退出
根据键盘输入，打印对应的信息
"""
while True:
    num = int(input())
    if num == 1:
        print("特遣队列表")
    elif num == 2:
        print("添加特遣队成员")
    elif num == 3:
        print("删除特遣队成员")
    elif num == 4:
        print("修改特遣队成员")
    elif num == 5:
        print("退出")
