import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)