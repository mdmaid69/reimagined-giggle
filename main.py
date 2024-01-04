import math
def calculate_error_function(x):
        return math.erf(x)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time