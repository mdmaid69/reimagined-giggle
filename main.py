import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_circle_area(radius):
        return math.pi * radius**2