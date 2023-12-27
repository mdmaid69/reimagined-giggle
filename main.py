def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)