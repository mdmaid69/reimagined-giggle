import collections
def create_ordered_dict():
        return collections.OrderedDict()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}