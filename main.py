def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import array
def get_array_buffer_info(array):
        return array.buffer_info()