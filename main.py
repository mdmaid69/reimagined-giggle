import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a