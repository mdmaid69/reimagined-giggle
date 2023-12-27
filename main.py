def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))