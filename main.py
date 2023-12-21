import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)