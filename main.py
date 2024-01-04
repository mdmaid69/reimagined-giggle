import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))