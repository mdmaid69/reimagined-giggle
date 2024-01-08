import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)