import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time