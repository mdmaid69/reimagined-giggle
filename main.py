import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time