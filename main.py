def calculate_volume(length, width, height):
        return length * width * height
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)