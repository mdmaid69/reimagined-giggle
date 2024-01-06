import math
def calculate_error_function(x):
        return math.erf(x)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal