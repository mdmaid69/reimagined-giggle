import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_perpetuity(payment, rate):
        return payment / rate