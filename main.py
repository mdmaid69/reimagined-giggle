import collections
def create_priority_queue():
        return collections.deque()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a