import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal