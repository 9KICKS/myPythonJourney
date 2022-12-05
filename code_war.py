def find_outlier(lst):
    odds = sum(value % 2 for value in lst[:3])
    target = int(odds < 2)
    return next(value for value in lst if value % 2 == target)
print(find_outlier([1,3,5,6,7,9]))
