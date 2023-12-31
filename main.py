import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time