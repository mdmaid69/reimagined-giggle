import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_area_circle(r):
        return 3.14 * r**2