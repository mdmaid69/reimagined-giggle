import array
def get_array_as_memoryview(array):
        return memoryview(array)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)