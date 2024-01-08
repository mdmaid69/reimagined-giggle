import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities