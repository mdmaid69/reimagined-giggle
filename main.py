def find_difference(list1, list2):
        return set(list1) - set(list2)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities