"""
使用if语句完成：
给定年龄，如果小于18岁，输出青少年，
如果大于等于18并且小于30岁，输出青年，
否则输出中老年
"""
while True:
    age = int(input("请输入年龄："))
    if age < 18:
        print("青少年")
    elif 18 <= age <30:
        print("青年")
    else:
        print("中老年")
