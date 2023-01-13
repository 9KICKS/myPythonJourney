def left_triangle(left):
    for i in range(0, left):
        for j in range(left - 1, i, -1):
            print(" ", end=' ')
        for i in range(0, i + 1):
            print("*", end=' ')
        print()


width = int(input("Enter the width of the left angled triangle: "))
left_triangle(width)

print()


def right_triangle(right):
    for i in range(0, right + 1):
        for j in range(0, i):
            print("*", end=' ')
        print(" ")


width = int(input("Enter the width of the right angled triangle: "))
right_triangle(width)

print()


def asterisks_diamond(diamond):
    for i in range(0, diamond):
        for j in range(0, diamond - i - 1):
            print(" ", end='')
        for k in range(0, 2 * i + 1):
            print("*", end='')
        print()
    for i in range(diamond - 1, 0, -1):
        for j in range(diamond, i, -1):
            print(" ", end='')
        for k in range(2 * i - 1, 0, -1):
            print("*", end='')
        print()


length = int(input("Enter the length of the diamond: "))
asterisks_diamond(length)

print()


def empty_diamond(empty):
    for i in range(1, empty + 1):
        for j in range(1, empty - i + 1):
            print(end=' ')
        for k in range(1, 2 * i):
            if k == 1 or k == i * 2 - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    for i in range(empty - 1, 0, -1):
        for j in range(1, empty - i + 1):
            print(' ', end='')
        for k in range(1, 2 * i):
            if k == 1 or k == i * 2 - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


length = int(input("Enter the length of the empty diamond: "))
empty_diamond(length)

print()


def empty_box(box_row, box_column):
    for i in range(0, box_row):
        for j in range(0, box_column):
            if i == 0 or i == box_row - 1 or j == 0 or j == box_column - 1:
                print('*', end='  ')
            else:
                print(' ', end='  ')
        print()


rows = int(input("Enter the rows of the box: "))
columns = int(input("Enter the columns of the box: "))
empty_box(rows, columns)
