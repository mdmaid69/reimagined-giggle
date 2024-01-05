import array
def get_array_as_frozenset(array):
        return frozenset(array)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps