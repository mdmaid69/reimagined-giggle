import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities