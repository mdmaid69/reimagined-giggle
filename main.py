import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)