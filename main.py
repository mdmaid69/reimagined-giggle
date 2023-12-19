import math
def calculate_permutations(n, k):
        return math.perm(n, k)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)