import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))