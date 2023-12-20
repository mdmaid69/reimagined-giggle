import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))