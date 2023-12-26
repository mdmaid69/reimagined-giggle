def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import re
def split_string(pattern, string):
        return re.split(pattern, string)