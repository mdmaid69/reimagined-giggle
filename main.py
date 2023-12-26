import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def get_array_as_frozenset(array):
        return frozenset(array)