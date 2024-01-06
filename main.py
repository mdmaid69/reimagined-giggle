import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_sign(x):
        return math.copysign(1, x)