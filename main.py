def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_remainder(x, y):
        return math.remainder(x, y)