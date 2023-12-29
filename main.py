import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)