import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)