import math
def calculate_sign(x):
        return math.copysign(1, x)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time