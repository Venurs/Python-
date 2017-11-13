"""
给定一个含有n个元素的整型数组a，如果元素出现的次数为奇数次，就输出
nums = [1, 2, 1, 2, 1, 3, 1, 4, 5, 3]
"""
nums = [1, 2, 1, 2, 1, 3, 1, 4, 5, 3, 4, 4]
num2 = []
for i in nums:
    if nums.count(i) % 2 == 1:
        num2.append(i)
print(set(num2))
