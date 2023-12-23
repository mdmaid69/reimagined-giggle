import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)