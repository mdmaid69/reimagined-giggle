import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))