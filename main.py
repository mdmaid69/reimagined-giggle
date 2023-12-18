import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets