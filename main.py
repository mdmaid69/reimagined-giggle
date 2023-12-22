def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)