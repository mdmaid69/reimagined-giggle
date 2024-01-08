import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets