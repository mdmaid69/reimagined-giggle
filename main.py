import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import collections
def create_counter():
        return collections.Counter()