def modify_list(lst):
    total_product = 1
    for element in lst:
        total_product *= element
    for i in range(len(lst)):
        lst[i] = int(total_product / lst[i])
    return lst


print(modify_list([1, 2, 3, 4]))
