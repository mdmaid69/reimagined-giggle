import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)