import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def remove_duplicates(lst):
        return list(set(lst))