import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities