import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def cube_number(x):
        return x**3