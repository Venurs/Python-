"""
打印1-100内，能被3整除，但不能被5整除的数，每行打印5个，并统计个数
"""
count = 1
while count <= 100:
    if count % 3 == 0 and count % 5 != 0:
        print(count, end=" ")
    count += 1
