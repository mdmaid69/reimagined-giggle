import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time