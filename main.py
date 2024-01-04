import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)