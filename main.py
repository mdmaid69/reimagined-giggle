import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)