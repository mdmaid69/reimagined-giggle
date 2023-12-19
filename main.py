import array
def get_bytes_from_array(array):
        return array.tobytes()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities