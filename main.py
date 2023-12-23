import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)