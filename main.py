def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)