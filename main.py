import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps