import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def square_number(x):
        return x**2