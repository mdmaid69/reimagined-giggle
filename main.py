import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)