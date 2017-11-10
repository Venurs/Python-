"""
输出1-100中7的倍数。
"""
count = 1
while count <= 100:
    if count % 7 == 0:
        print(count, end=" ")
    count += 1
