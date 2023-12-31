import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time