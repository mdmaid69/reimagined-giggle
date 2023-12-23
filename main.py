import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding