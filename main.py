import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities