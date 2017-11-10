"""
求1-100内所有奇数的和
"""
count = 1
sub = 0
while count <= 100:
    sub += count
    count += 2
print(sub)
