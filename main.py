from collections import Counter
print(Counter("hello world"))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)