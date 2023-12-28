import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_area(radius):
        return 3.14 * radius * radius