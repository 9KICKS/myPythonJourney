def maximum_sublist_sum(array):
    maximum_sum = array[0]
    current_sum = array[0]
    for i in range(1, len(array)):
        current_sum = max(array[i], current_sum + array[i])
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


print(maximum_sublist_sum([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
