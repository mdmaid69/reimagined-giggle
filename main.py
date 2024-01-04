import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))