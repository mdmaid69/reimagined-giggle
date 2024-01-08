import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time