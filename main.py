def find_union(list1, list2):
        return set(list1) | set(list2)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))