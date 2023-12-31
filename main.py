import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time