import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)