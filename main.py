import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import collections
def count_elements(iterable):
        return collections.Counter(iterable)