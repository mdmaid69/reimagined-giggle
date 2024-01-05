import math
def calculate_permutations(n, k):
        return math.perm(n, k)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time