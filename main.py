import math
def calculate_logarithm(base, x):
        return math.log(x, base)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time