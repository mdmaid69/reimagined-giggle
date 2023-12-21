import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a