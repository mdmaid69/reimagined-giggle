import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def convert_to_octal(n):
        return oct(n)