import array
def get_array_as_frozenset(array):
        return frozenset(array)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)