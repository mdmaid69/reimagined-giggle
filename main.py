import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)