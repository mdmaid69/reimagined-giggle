import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets