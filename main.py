import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def count_elements(lst):
        return len(lst)