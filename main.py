def is_even(n):
        return n % 2 == 0
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)