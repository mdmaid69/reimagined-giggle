import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)