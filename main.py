import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time