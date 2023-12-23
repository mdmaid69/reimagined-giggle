import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))