import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time