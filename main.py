import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import collections
def count_elements(iterable):
        return collections.Counter(iterable)