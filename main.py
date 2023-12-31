import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)