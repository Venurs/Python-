"""
火车站安检
has_ticket,布尔型，是否有车票
knife_length,表示刀的长度，单位：厘米
检查是否有车票，如果有才允许进行安检
安检时，检查刀的长度是否超过20cm，如果不超过，安检通过
否则不允许上车
没有车票，不允许进门
"""
while True:
    has_ticket = bool(input("是否有车票？"))
    knife_length = int(input("请输入刀的长度："))
    if has_ticket:
        print("允许进门以及安检")
        if knife_length > 20:
            print("安检不通过")
        else:
            print("可以上车")
    else:
        print("没有车票，不能进门")
