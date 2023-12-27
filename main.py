import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)