import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding