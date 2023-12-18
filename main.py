import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)