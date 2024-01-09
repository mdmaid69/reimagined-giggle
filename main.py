def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))