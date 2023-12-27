import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets