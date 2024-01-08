import math
def calculate_error_function(x):
        return math.erf(x)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time