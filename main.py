def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)