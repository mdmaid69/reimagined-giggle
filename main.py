import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities