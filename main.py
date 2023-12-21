import math
def calculate_gamma_function(x):
        return math.gamma(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)