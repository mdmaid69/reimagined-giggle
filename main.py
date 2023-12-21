import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)