import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time