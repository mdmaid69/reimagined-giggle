import collections
def create_queue():
        return collections.deque()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable