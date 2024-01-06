import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))