import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity