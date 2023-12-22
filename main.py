import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time