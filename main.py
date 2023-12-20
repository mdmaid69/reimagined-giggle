import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)