import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time