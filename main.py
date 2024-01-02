import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)