import array
def get_array_as_memoryview(array):
        return memoryview(array)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))