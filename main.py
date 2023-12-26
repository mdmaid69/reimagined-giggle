def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))