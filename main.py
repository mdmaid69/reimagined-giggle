import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))