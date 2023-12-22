def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)