"""
女朋友的节日
holiday_name ,记录几日的名字
情人节：买玫瑰，看电影
平安夜：买苹果，吃大餐
生日：买蛋糕
其他的日期每天都是节日啊。。
"""
while True:
    holiday_name = input("请输入节日名：")
    if holiday_name == "情人节":
        print("买玫瑰，看电影")
    elif holiday_name == "平安夜":
        print("买苹果，吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日呀。。。。mmp")

