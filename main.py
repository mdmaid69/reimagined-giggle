import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time