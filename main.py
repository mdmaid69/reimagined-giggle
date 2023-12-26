import array
def get_list_from_array(array):
        return array.tolist()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities