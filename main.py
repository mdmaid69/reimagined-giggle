import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity