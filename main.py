import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time