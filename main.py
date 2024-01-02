def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
def remove_duplicates(lst):
        return list(set(lst))