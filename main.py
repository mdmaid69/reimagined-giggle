import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)