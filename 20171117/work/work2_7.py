"""
传入多个参数(数字和字符串)，如果是数字累加和，如果是字符串进行拼接
"""


def funcation(*values):
    number = 0
    string = ""
    for value in values:
        if isinstance(value, int):
            number += value
        elif isinstance(value, str):
            string += value
    return number, string


print(funcation(2, "s", "d", "f", 6, 3, "g", 5, "h", 4, "j", "r"))
