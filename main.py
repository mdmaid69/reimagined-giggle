def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))