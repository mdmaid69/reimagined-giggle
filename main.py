import math
def calculate_exponential(x):
        return math.exp(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)