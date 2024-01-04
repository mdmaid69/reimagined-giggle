import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time