import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time