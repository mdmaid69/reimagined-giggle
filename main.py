import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)