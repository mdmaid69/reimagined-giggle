import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import math
def calculate_circle_area(radius):
        return math.pi * radius**2