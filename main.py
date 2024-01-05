def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)