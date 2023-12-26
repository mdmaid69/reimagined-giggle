import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))