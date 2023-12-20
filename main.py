import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_average(lst):
        return sum(lst) / len(lst)