"""
模拟登录，键盘上输入用户名和密码，如果用户名是admin密码是123，
或者用户名是zhangsan密码是zhangsan123，
都表示可以登录。
否则打印登录失败
"""
while True:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if (name == "admin" and password == "123") or (name == "zhangsan" and password == "zhangsan123"):
        print("登陆成功")
    else:
        print("登陆失败")
