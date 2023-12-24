def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)