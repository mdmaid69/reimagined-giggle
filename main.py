for i in range(10): print(i)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)