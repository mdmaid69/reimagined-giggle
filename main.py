import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))