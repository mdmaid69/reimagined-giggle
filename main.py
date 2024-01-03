import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)