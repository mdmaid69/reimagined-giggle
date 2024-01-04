import math
def calculate_error_function(x):
        return math.erf(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)