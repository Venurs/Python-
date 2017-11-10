"""
验证键盘输入的用户名和密码，是否是admin和123456，判断是否登录成功
"""
user_name = input()
password = input()
if user_name == "admin" and password == "123456":
    print("登陆成功")
else:
    print("登陆失败")
