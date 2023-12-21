import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps