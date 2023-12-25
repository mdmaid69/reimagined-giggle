import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import collections
def count_elements(iterable):
        return collections.Counter(iterable)