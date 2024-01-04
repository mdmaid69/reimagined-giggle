import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps