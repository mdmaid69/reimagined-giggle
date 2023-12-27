import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities