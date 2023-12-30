import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)