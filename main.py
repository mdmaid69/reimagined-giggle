import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import collections
def create_stack():
        return collections.deque()