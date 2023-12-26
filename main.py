import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)