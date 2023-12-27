import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)