import re
def split_string(pattern, string):
        return re.split(pattern, string)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)