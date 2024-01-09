import collections
def create_queue():
        return collections.deque()
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)