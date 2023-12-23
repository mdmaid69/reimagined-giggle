def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)