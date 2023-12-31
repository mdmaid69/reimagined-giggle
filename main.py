import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)