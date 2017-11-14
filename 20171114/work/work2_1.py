"""
ECALIYHWEQAEFSZCVZTWEYXCPIURVCSWTDBCIOYXGTEGDTUMJHUMBJKHFGUKNKN
每个字母出现的次数
提示：字典{字母：count}
"""
str1 = "ECALIYHWEQAEFSZCVZTWEYXCPIURVCSWTDBCIOYXGTEGDTUMJHUMBJKHFGUKNKN"
dict1 = dict()
for i in str1:
    if i not in dict1.keys():
        dict1[i] = str1.count(i)
print(dict1)




