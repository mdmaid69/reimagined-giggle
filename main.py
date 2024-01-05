import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)