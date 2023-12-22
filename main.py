import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities