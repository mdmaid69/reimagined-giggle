import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)