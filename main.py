import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets