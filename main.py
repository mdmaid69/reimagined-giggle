def find_min(lst):
        return min(lst)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))