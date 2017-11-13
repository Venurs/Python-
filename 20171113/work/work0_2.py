"""
给定一个以下字符串：统计大写字母的个数，小写字母的个数，非字母的个数。多种算法完成。
str1 = "ajdkkKDKEK1343KFKiriromfkfKKRIOWJF0928398jjee11djdDJJRH"
"""


str = "ajdkkKDKEK1343KFKiriromfkfKKRIOWJF0928398jjee11djdDJJRH"


big = small = letter = 0
for i in str:
    if i.islower():
        small += 1
    elif i.isupper():
        big += 1
    elif i.isalpha():
        letter += 1
print(big, small, len(str) - letter)
