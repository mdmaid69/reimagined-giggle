import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities