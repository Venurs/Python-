"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""


def put(m, bor):
    count = 1
    while count < 2 * bor:
        if (bor == count) or ((bor - m) < count < (bor + m)):
            print("*", end="")
        else:
            print(" ", end="")
        count += 1
    print()


border = int(input())
i = 1
while i <= border:
    put(i, border)
    i += 1
j = border - 1
while j >= 1:
    put(j, border)
    j -= 1
