import array
def get_array_as_memoryview(array):
        return memoryview(array)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities