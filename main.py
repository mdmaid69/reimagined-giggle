def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)