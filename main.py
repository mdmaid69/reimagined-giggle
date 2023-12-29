import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)