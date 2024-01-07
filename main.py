import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding