import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)