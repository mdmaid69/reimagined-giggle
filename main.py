import collections
def create_queue():
        return collections.deque()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)