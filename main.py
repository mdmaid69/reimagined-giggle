import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)