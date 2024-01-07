import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))