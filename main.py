def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)