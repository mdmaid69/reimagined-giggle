import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities