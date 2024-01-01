import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time