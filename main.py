import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps