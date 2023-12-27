import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)