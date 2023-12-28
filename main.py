import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities