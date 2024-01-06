import math
def calculate_logarithm(base, x):
        return math.log(x, base)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)