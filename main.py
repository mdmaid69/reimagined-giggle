def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)