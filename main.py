import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities