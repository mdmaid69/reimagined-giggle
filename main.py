import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)