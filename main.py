import math
def calculate_arc_cosine(x):
        return math.acos(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)