import array
def convert_array_to_list(array):
        return array.tolist()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities