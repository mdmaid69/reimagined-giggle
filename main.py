import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))