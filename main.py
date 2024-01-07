import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal