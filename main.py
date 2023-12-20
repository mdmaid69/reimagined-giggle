import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps