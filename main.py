import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def add_numbers(a, b):
        return a + b