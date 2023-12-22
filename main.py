import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)