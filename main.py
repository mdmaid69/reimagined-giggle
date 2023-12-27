import math
def calculate_floor(x):
        return math.floor(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)