import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)