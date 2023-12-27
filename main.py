import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time