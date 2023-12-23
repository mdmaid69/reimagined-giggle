import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time