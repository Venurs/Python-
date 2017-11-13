"""
给定一个路径名：
String pathName="http://192.168.10.1:8080/Day33_Servlet/aa.jpeg";
获取文件名称：aa.jpeg
"""
pathName = "http://192.168.10.1:8080/Day33_Servlet/aa.jpeg"
count = len(pathName) - 1
while count >= 0:
    if pathName[count] == "/":
        print(pathName[count + 1:])
        break
    count -= 1


