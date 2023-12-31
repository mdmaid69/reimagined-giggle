import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_combinations(n, k):
        return math.comb(n, k)