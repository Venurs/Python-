"""
模拟超市付款： 商品单价   商品数量
键盘上输入商品单价，以及商品数量，
然后计算应付总额
计算总额  double
提示用户可以有4种付款方式
不同的付款方式有不同的折扣:
 先展示四种付款方式
现金没有折扣
微信 0.95折
支付宝 鼓励金付款金额的10%   鼓励金可以直接折算到付款金额中
刷卡 满100-20   (int)(659/100)  6*20=120    659-120=
"""
print("付款方式：")
print("\t现金没有折扣\t")
print("\t微信 0.95折\t")
print("\t支付宝 鼓励金付款金额的10%   鼓励金可以直接折算到付款金额中\t")
print("\t刷卡 满100-20   (int)(659/100)  6*20=120    659-120=\t")
while True:
    price = float(input("请输入商品单价："))
    num = int(input("请输入商品数量："))
    money = price * num
    way = int(input("请输入付款方式："))
    if way == 1:
        print("应付金额：%.1f" % money)
    elif way == 2:
        money = 0.95 * money
        print("应付金额：%.1f" % money)
    elif way == 3:
        money = 0.9 * money
        print("应付金额：%.1f" % money)
    elif way == 4:
        if money >= 100:
            money = money - int(money / 100) * 20
            print("应付金额：%.1f" % money)
