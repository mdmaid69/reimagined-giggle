import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_acceleration(speed, time):
        return speed / time