import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_pressure(force, area):
        return force / area