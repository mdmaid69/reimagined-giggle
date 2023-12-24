def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)