import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import collections
def count_elements(iterable):
        return collections.Counter(iterable)