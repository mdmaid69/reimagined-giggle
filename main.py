import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal