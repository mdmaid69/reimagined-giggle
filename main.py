import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))