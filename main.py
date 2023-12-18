import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time