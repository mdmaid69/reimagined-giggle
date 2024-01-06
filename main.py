import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}