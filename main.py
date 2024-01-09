import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time