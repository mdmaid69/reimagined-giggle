import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)