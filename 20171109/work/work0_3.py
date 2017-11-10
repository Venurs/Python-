"""
操场上有一群人，人数在100到200之间。三人一组多1人，四人一组多2人，五人一组多3人
"""
count = 100
while count <= 200:
    if (count - 1) % 3 == 0 and (count - 2) % 4 == 0 and (count - 3) % 5 == 0:
        print(count)
    count += 1

