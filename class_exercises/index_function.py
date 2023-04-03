def get_index(x, y, z):
    total = 0
    i = 0

    while total < y:
        i += 1
        total += x

    if total == y and i > 0 and (i * x) - (x - z) <= y:
        return i
    else:
        return - 1


x = 3
y = 12
z = 1
print("Result = ", get_index(x, y, z))
