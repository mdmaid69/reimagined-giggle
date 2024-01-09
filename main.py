import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))