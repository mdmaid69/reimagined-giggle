import collections
def create_ordered_dict():
        return collections.OrderedDict()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)