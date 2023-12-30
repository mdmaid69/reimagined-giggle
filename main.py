import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)