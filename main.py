def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)