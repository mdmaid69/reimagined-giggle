import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal