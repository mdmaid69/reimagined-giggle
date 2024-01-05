import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)