import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))