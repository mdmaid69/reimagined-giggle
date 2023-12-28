def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))