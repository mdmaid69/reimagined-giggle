def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)