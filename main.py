import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time