import collections
def create_counter():
        return collections.Counter()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))