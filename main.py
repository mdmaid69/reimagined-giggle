def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)