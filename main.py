def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))