import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)