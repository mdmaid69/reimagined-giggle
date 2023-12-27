import array
def convert_array_to_unicode(array):
        return array.tounicode()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities