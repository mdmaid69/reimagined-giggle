import math
def calculate_square_root(x):
        return math.sqrt(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)