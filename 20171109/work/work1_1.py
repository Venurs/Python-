"""
某电话公司电话收费有3个套餐
A.月租50元，包100分钟，超出100分钟，1元/分，200元封顶。
B.月租50元，包100分钟，超出100分钟，0.85元/分，不封顶
C.无月租，0.75元/分，不封顶。
根据用户输入的通话时长，为用户推荐最优惠的套餐。
"""
time = int(input("请输入通话时长："))
money_a = 50 + (time - 100) * 1
money_b = 50 + (time - 100) * 0.85
money_c = time * 0.75
print(money_a, money_b, money_c)
if money_b > 200 or money_c > 200:
    print("A吧")
elif money_b > money_c:
    print("C吧")
elif time < 100:
    print("A B任选")
else:
    print("B吧")

