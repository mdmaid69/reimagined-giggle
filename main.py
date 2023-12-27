import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import collections
def count_elements(iterable):
        return collections.Counter(iterable)