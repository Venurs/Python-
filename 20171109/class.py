"""
从1-50中，找一个：能被3整除，不能被5整除
。找到一个即可。输出结果
练习1：使用while循环，验证键盘输入的用户名和密码，验证失败3次，锁定账户。
用户名：admin，密码：123abc

练习2：猜数：
系统产生一个随机数：33
[1,100]
玩家猜：
50,猜大了，
玩家猜：
10，猜小了
玩家猜：33
猜对了。。。
sys_num = 33

while True:
step1：接收用户猜的数
step2：根系统产生的随机数进行比较：大，小
对了：强制结束循环：break

"""
# count = 1
# while count <= 50:
#     if count % 3 == 0 and count % 5 != 0:
#         print(count)
#         break
#     count += 1


# sum1 = 0
# while True:
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     if name != "admin" or password != "123":
#         sum1 += 1
#         print("登陆失败")
#     else:
#         print("登陆成功")
#     if sum1 == 3:
#         print("账户锁死")
#         break

# import random
# num = random.randint(1, 100)
# while True:
#     num2 = int(input("输入你猜的数："))
#     if num < num2:
#         print("你猜大了")
#     elif num > num2:
#         print("你猜小了")
#     elif num == num2:
#         print("你猜对了")
#         break

# i = 0
#
# while i < 5:
#     j = 0
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1


