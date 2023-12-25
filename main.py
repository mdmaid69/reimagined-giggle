import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)