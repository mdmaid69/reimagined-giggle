import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time