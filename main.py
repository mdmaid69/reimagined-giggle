import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))