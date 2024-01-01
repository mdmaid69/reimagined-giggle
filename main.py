import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)