import collections
def create_stack():
        return collections.deque()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)