import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)