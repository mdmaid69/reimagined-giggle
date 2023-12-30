def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))