import math
"""
定义一个函数，通过参数，接收3个边长，求三角形的面积
百度：海伦公式
"""


def is_trigon(c, k, g):
    if c + k > g and c + g > k and g + k > c and c - k < g and c - g < k and g - k < c:
        return True
    return False


def area(c, k, g):
    if is_trigon(c, k, g):
        perimeter = (c + k +g)/ 2
        area = math.sqrt(perimeter * (perimeter - c) * (perimeter - k) * (perimeter - g))
        return area
    else:
        return "无法构成三角形"


c = int(input("请输入长"))
k = int(input("请输入宽"))
g = int(input("请输入边"))
print(area(c,  k, g))

