import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets