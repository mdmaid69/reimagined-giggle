import math
def calculate_sign(x):
        return math.copysign(1, x)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)