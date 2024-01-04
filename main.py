def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)