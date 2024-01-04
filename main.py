import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities