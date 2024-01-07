import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time