import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time