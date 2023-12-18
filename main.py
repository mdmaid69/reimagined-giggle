import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time