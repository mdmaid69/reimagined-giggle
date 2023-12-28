import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time