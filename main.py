import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)