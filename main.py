import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)