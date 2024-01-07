import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)