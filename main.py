import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps