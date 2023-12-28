list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))