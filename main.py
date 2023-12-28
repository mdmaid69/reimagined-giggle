import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time