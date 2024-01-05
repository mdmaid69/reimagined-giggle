import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets