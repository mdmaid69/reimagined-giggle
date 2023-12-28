import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def get_array_buffer_info(array):
        return array.buffer_info()