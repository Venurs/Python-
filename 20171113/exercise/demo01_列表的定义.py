"""
列表：list
    1.概念：用于存储一组数据。使用[]。类似于其他语言的数组

    2.使用：
        语法声明：[元素1,元素2,元素3....]
        可以通过下标索引来获取指定的元素：index，从0开始到长度减1
            下标：也可以为负：-1代表最后一个，-2代表倒数第二个，依此类对。。
    3.特点：
        A：列表中存储的元素是有顺序，且数据可以重复
        B：一个列表 中可以存储多个任意类型的元素，但实际上一般只存储一种类型的数据
"""
# 1.定义一个列表，存储多个数值
nums = [10, 20, 30, 20]
print(nums)
print(len(nums))
print(type(nums))  # <class 'list'>

# 2.获取列表中的数据
print(nums[0])
print(nums[1])
# print(nums[3])  # IndexError: list index out of range
print(nums[-1])

# 3.遍历列表：
for i in nums:
    print(i)  # 10,20,30

index = 0
while index < len(nums):
    print(nums[index], end="\t")
    index += 1

print("------")
names = ["王二狗", "李小花", "三胖", "Rose", "Jack", "Tom", "Jerry"]
print(names)
