import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)