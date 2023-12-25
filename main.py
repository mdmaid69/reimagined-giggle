def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}