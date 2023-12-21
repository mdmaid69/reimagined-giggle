def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)