print([x**2 for x in range(10)])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)