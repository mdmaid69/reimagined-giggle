import math
def calculate_error_function(x):
        return math.erf(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)