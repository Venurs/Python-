"""
字符串str="ABCDEFGHIJK"，
要求输出最少一个最多八个的所有组合（向后连续字母）
"""

str1 = "ABCDEFGHIJK"
for i in range(0, len(str1)):
    for j in range(i, i + 9):
        if j <= len(str1):
            print(str1[i:j], end=" ")

    print()
