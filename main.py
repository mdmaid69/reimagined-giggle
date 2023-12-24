import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable