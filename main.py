import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_circle_area(radius):
        return math.pi * radius**2