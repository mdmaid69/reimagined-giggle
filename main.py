import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)