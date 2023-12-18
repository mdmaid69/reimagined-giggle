import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities