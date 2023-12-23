import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time