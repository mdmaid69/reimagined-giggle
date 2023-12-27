import math
def calculate_sign(x):
        return math.copysign(1, x)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)