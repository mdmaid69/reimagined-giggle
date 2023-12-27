import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time