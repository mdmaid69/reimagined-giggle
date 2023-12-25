import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
from collections import Counter
print(Counter("hello world"))