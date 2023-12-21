import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)