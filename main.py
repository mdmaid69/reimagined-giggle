import array
def get_array_as_complex(array):
        return complex(array[0])
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities