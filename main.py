import math
def calculate_sine(x):
        return math.sin(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)