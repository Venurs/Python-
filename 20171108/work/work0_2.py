"""
使用if语句完成：给定数字：如果为1，就输出星期一，
如果为2，就输出星期二，
以此类推，一直到7，输出星期日。
如果是其他数字，就输出"错误信息"。
"""
date = int(input())
if date == 1:
    print("星期一")
elif date == 2:
    print("星期二")
elif date == 3:
    print("星期三")
elif date == 4:
    print("星期四")
elif date == 5:
    print("星期五")
elif date == 6:
    print("星期六")
elif date == 7:
    print("星期日")
else:
    print("错误信息")
