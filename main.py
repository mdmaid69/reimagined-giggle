def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)