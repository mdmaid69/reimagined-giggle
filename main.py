def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)