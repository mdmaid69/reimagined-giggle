import collections
def create_counter():
        return collections.Counter()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))