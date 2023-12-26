import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal