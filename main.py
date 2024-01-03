import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities