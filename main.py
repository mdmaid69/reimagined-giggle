import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)