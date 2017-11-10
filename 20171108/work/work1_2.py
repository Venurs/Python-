"""
int money = ...;
如果money>1000000(一百万),
输出“。。。。。。”
否则输出“。。。。。”
"""
while True:
    money = int(input("输入比的钱数："))
    if money > 1000000:
        print("你特么的真有钱")
    else:
        print("穷逼")
