"""
一个四位数，恰好等于去掉它的首位数字之后所剩的三位数的3倍，这个四位数是多少
"""
count = 1000
while count <= 9999:
    num = count
    num = num % 1000
    if num * 3 == count:
        print(count)
    count += 1
