"""
用if语句完成：
从键盘输入考试分数(整数)，
如果成绩大于等于90，输出学霸实在牛，
如果大于等于80，输出学神要加油，
如果大于等于70，输出学民好害羞，
如果大于等于60输出学弱打酱油，
如果小于60，输出学渣泪在流。
"""
while True:
    score = int(input("输入你的分数："))
    if score >= 90:
        print("学霸真是牛")
    elif score >= 80:
        print("学神要加油")
    elif score >= 70:
        print("学民好害羞")
    elif score >= 60:
        print("学弱打酱油")
    elif score < 60:
        print("学渣泪在流")
