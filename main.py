import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import array
def set_array_item(array, i, item):
        array[i] = item