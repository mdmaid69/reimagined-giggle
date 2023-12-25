import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import re
def split_string(pattern, string):
        return re.split(pattern, string)