import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))