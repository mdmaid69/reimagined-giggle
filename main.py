import collections
def create_stack():
        return collections.deque()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)