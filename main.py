def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))