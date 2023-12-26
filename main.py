def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)