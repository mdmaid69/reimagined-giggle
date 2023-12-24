import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))