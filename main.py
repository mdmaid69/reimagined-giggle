import math
def calculate_sign(x):
        return math.copysign(1, x)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities