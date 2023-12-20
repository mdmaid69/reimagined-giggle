import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)