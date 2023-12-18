import math
def calculate_sign(x):
        return math.copysign(1, x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)