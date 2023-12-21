import math
def calculate_absolute_value(x):
        return math.fabs(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)