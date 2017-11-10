"""
有一个两位数，如果在它的前面添加一个3，
可以得到一个三位数，把3添加在它的后面，
也可以得到一个三位数。这两个三位数相差468，
求原来的两位数
"""
count = 10
while count <= 99:
    num1 = int("3" + str(count))
    num2 = int(str(count) + "3")
    if num1 - num2 == 468 or num2 - num1 == 468:
        print(count)
    count += 1
