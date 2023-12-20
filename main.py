import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))