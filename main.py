import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities