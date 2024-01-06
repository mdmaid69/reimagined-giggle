import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)