import collections
def create_priority_queue():
        return collections.deque()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a