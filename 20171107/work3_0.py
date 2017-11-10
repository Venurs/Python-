"""
假设登录途牛网站，买票
可以通过账号登录
也可以手机号码登录 + 密码
账户：feizhu123
手机号：18067451231，密码 123456
"""
user_name = input()
password = input()
if password != "123456":
    print("登陆失败")
elif user_name == "feizhu123" or user_name == "18067451231":
    print("登陆成功")
else:
    print("登陆失败")
