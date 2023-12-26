import re
def split_string(pattern, string):
        return re.split(pattern, string)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)