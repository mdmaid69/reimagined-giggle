import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)