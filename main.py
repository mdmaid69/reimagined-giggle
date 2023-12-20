import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)