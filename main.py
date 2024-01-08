import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal