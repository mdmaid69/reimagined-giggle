def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))