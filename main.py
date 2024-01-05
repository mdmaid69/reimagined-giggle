import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)