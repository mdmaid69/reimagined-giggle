def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable