import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import collections
def create_counter():
        return collections.Counter()