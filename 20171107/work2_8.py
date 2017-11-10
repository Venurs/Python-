"""
关系运算符
"""

a, b, c = 15, 10, 7
res = (a > --b+c) and (c + 1 < b - 1 + (--a))
res2 = (a > --b+c) or (c + 1 < b - 1+(--a))
print(res, res2)

