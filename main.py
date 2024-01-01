import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))