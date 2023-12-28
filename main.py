import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)