import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets