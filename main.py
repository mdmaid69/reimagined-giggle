import collections
def create_queue():
        return collections.deque()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)